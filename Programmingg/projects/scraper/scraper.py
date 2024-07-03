#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import pymongo
import logging

# Set up logging
logging.basicConfig(filename='/var/log/hostel_scraper.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

try:
    # Set up MongoDB connection
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["hostel_db"]
    collection = db["hostels"]

    # Prep up the web driver
    options = Options()
    options.add_argument('-headless')   # Run Firefox in headless mode (no GUI)
    service = Service()
    driver = webdriver.Firefox(service=service, options=options)

    # Make url "dynamic" to avoid err in GET request
    today = datetime.now()
    checkin = (today + timedelta(days=1)).date()
    checkout = (today + timedelta(days=5)).date()
    url = f"https://www.hostelworld.com/pwa/wds/s?q=Chiang%20Mai,%20Thailand&country=Chiang%20Mai&city=Chiang%20Mai&type=city&id=831&from={checkin}&to={checkout}&guests=1&page=1&sort=lowestprice"
    driver.get(url)

    # Wait until the hostel cards are loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'property-card-container')))

    # Get hostel cards
    hostel_cards = driver.find_elements(By.CLASS_NAME, 'property-card-container')

    # Extract needed information from each card
    for card in hostel_cards:
        name = card.find_element(By.CLASS_NAME, 'property-name').text.strip()
        link = card.get_attribute('href')
        
        # Extract dorm price
        price_divs = card.find_elements(By.CLASS_NAME, 'property-accommodation-price')
        dorm_price = "N/A"
        for price_div in price_divs:
            if 'Dorms From' in price_div.text:
                dorm_price = price_div.find_element(By.CLASS_NAME, 'current').text.strip()
                break
        
        # Check if hostel exists in database
        existing_hostel = collection.find_one({"name": name})
        
        if existing_hostel:
            if existing_hostel["dorm_price"] != dorm_price:
                # Update the hostel information
                collection.update_one(
                    {"name": name},
                    {"$set": {"link": link, "dorm_price": dorm_price, "last_updated": today}}
                )
                logging.info(f"Updated {name} - New price: {dorm_price}")
            else:
                logging.info(f"No price change for {name}")
        else:
            # Insert new hostel
            collection.insert_one({
                "name": name,
                "link": link,
                "dorm_price": dorm_price,
                "last_updated": today
            })
            logging.info(f"Added new hostel: {name}")

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")

finally:
    # Close web driver
    if 'driver' in locals():
        driver.quit()
    # Close db connection
    if 'client' in locals():
        client.close()
    logging.info("Scraping completed")

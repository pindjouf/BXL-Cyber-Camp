# Hostel Scraper

This project is a web scraper that extracts information about hostels in Chiang Mai, Thailand from Hostelworld.com. It stores the data in a MongoDB database and logs the results. This project was created as a learning exercise for working with NoSQL databases.

It's meant to be run as a cronjob on a server to find the best prices.

## Features

- Scrapes hostel data from Hostelworld.com
- Stores data in a MongoDB database
- Updates existing entries if prices change
- Logs all actions and errors

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- MongoDB installed and running
- Firefox browser installed (the script uses Firefox in headless mode)

## Installation

Good luck.

## Usage

1. Make sure MongoDB is running on your system.

2. Run the script:
   ```
   python scraper.py
   ```

   Note: You may need to run it with sudo if the script needs to write to system log files:
   ```
   sudo python scraper.py
   ```

3. The script will scrape the hostel data, store it in the MongoDB database, and log its actions.

## Configuration

- The MongoDB connection string is set to `"mongodb://localhost:27017/"`. If your MongoDB is running on a different host or port, update this in the script. Like if it's in a container for example.
- The log file is set to `/var/log/hostel_scraper.log`. You may need to change this path or ensure you have write permissions.

## Project Structure

- `scraper.py`: The main Python script that performs the web scraping and database operations.
- `README.md`: This file, containing project documentation.

## Learning Outcomes

This project demonstrates:
- Web scraping using Selenium
- Working with NoSQL databases (MongoDB)
- Handling date and time in Python
- Error handling and logging in Python
- Using headless browsers for web scraping

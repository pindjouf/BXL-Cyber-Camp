# Phishing Campaign

## Overview

This phishing campaign is designed to target individuals with specific interests, namely Bob, who loves dogs, and Alice, who loves cars. The campaign will utilize tailored emails to appeal to their interests, leading them to click on a fake Amazon login page, where they will be prompted to enter their credentials. The ultimate goal is to acquire their login credentials through the fake page.

### *Things to keep in mind*
This is an MVP (Minimum Viable Product) so the goal is mostly to get something out there that works in my local environment (for now). See footer for a list of tasks that would make the product better.

## Target Audience

- **Bob**: A dog lover who owns a bull terrier named "Shimi". Bob's affinity for his dog will be leveraged in the email content to increase the likelihood of engagement.

- **Alice**: An enthusiast of vintage cars, particularly a fan of Mécanique. Alice owns two vintage cars and enjoys showcasing her ancestral objects. The email content will reflect her passion for cars to entice her to click on the phishing link.

## Approach

### Email Content

- **Bob's Email**: The email to Bob will emphasize his love for dogs and offer enticing dog-related products available on Amazon.

- **Alice's Email**: Alice will receive an email focusing on her passion for cars, featuring vintage car accessories and Mécanique-themed items available on Amazon.

### Phishing Page

A custom Amazon login page will be created to mimic the authentic Amazon login interface. The page will prompt users to enter their credentials, which will be captured through a web hook.

### Execution

1. **Email Crafting**: Tailor the email content for Bob and Alice, ensuring it resonates with their respective interests.

2. **Phishing Page Development**: Develop the fake Amazon login page, ensuring it closely resembles the authentic Amazon interface to deceive the recipients.

3. **Email Deployment**: Send the crafted emails to Bob and Alice's email addresses.

4. **Monitoring**: Monitor engagement rates and click-throughs to gauge the effectiveness of the campaign.

5. **Credential Capture**: Capture login credentials entered on the fake Amazon login page using a web hook.

6. **Analysis**: Analyze captured credentials and assess the success of the campaign.

### Structure

    /campaign
    |
    |-- /alice
    |   -- alice.eml
    |
    |-- /asssets
    |   -- screenshots.md
    |
    |-- /bob
    |   -- bob.eml
    |
    -- README.md
    -- index.html
    -- store.html


### Footer / Useful Additions / Things to be done

- Make the links in the emails redirect to an actual page
- Git push the actual .eml file and not just the html

## Disclaimer

**Important**: This phishing campaign is for educational purposes only and must not be used for any malicious intent. Engaging in unauthorized access to computer systems or data is illegal and unethical. Always ensure compliance with applicable laws and regulations.

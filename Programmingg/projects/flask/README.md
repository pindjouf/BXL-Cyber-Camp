# Hackers Poulette Form

This repository contains a simple web application built with Flask that provides a contact form. When the form is submitted, the data is sanitized and stored in a SQLite database. This document explains how to set up and run the application.

## Features

- Displays a contact form.
- Sanitizes user inputs to prevent XSS attacks.
- Stores contact form submissions in a SQLite database.
- Uses environment variables for database configuration.

## Requirements

- Python 3.x
- Flask
- SQLite3
- python-dotenv
- bleach

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/pindjouf/BXL-Cyber-Camp
    cd BXL-Cyber-Camp/Programmingg/projects/flask
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your SQLite database path:

    ```plaintext
    DB=path/to/your/database.db
    ```

5. Ensure you have a SQLite database with a table named `contact`:

    ```sql
    CREATE TABLE contact (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        country TEXT NOT NULL,
        message TEXT NOT NULL,
        gender TEXT NOT NULL,
        subject TEXT NOT NULL,
        timestamp TEXT NOT NULL
    );
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the contact form.

3. Fill out the form and submit it. The data will be sanitized and stored in the database.

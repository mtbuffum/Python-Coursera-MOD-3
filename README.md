# README

## Overview
This repository contains three Python scripts, two of which serve as practice exercises to learn about Python libraries, and one that is part of the Google Python Coursera module challenge.

## Scripts

### 1. **Car Sales Report (Google Python Coursera Challenge)**
- **Filename:** `car_sales_report.py`
- **Purpose:** This script processes car sales data from a JSON file, generates a summary report, and emails it as a PDF attachment.
- **Key Functionalities:**
  - Loads and processes data from a JSON file.
  - Determines the most popular car model, best-selling year, and highest revenue.
  - Generates a PDF report using `reportlab`.
  - Sends the report via email using the `emails` module.
- **Libraries Used:** `collections`, `json`, `locale`, `mimetypes`, `os.path`, `reports`, `sys`, `emails`

### 2. **Email Practice Script**
- **Filename:** `email_practice.py`
- **Purpose:** This script is a practice exercise for sending emails using Python.
- **Key Functionalities:**
  - Creates an email using `email.message.EmailMessage`.
  - Sends the email using `smtplib.SMTP_SSL`.
  - Prompts the user for their email application password securely using `getpass`.
- **Libraries Used:** `email.message`, `smtplib`, `getpass`

### 3. **PDF Report Practice Script**
- **Filename:** `pdf_practice.py`
- **Purpose:** This script is a practice exercise for generating PDF reports using `reportlab`.
- **Key Functionalities:**
  - Generates a PDF document titled "A Complete Inventory of My Fruit".
  - Creates and formats a table of fruit names and their quantities.
  - Generates a pie chart visualizing the fruit data.
- **Libraries Used:** `reportlab.platypus`, `reportlab.lib.styles`, `reportlab.lib.colors`, `reportlab.graphics.shapes`, `reportlab.graphics.charts.piecharts`, `reportlab.lib.units`

## How to Use
1. **Car Sales Report Script:**
   - Ensure `car_sales.json` is present in the same directory.
   - Run the script: `python car_sales_report.py`
   - The script will generate a PDF report and email it.

2. **Email Practice Script:**
   - Update the sender and recipient email addresses.
   - Enable "App Passwords" for Gmail if using a Gmail account.
   - Run the script: `python email_practice.py`
   - Enter your email application password when prompted.

3. **PDF Report Practice Script:**
   - Run the script: `python pdf_practice.py`
   - The script will generate a `report.pdf` file in the same directory.

## Prerequisites
Ensure you have the following Python libraries installed before running the scripts:
```sh
pip install reportlab
```
For email functionality:
```sh
pip install secure-smtplib
```

## Notes
- The practice scripts help familiarize with sending emails and generating PDF reports in Python.
- The Coursera challenge script is a real-world application integrating JSON data processing, PDF generation, and email automation.
- Modify the email addresses and SMTP settings according to your requirements before running the scripts.

## Author
Mason

---
This repository serves as a learning resource and a demonstration of Python scripting capabilities in automation and reporting.


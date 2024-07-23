# Zillow Scraper and Form Filler Bot

This project is designed to scrape real estate data from Zillow and automatically fill a Google Form with the collected data. The bot uses Beautiful Soup for web scraping and Selenium for interacting with the web form.

## Features

- Scrapes real estate prices, links, and addresses from Zillow.
- Automatically inputs the scraped data into a specified Google Form.
- Utilizes Beautiful Soup for web scraping and Selenium for web automation.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup4
- requests_html
- Google Chrome
- ChromeDriver

## Installation

1. Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the project directory.

2. Create a `config.json` file in the project directory with the following structure:

   ```json
   {
     "zillow_link": "YOUR_ZILLOW_SEARCH_URL",
     "forms_link": "YOUR_GOOGLE_FORM_URL",
     "driver_path": "PATH_TO_YOUR_CHROMEDRIVER"
   }
   ```

## Usage

1. Open the `config.json` file and fill in the appropriate URLs and driver path.
2. Run the script:

   ```bash
   python main.py
   ```

## How It Works

1. **Web Scraping with Beautiful Soup**: The script first uses Beautiful Soup to scrape real estate data from Zillow. It collects prices, links, and addresses of the properties listed.

   ```python
   def getting_prices():
       # Implementation for scraping prices
   ```

   ```python
   def getting_links():
       # Implementation for scraping property links
   ```

   ```python
   def getting_addresses():
       # Implementation for scraping property addresses
   ```

2. **Form Filling with Selenium**: The script then uses Selenium to automate the process of filling out a Google Form with the scraped data.

   ```python
   class EnteringDataIntoForms:
       def __init__(self, data):
           # Initialization code

       def data_into_forms(self):
           # Code to fill the form with scraped data
   ```

3. **Main Execution**: The main part of the script reads the configuration from the `config.json` file, initializes the form filler bot, and starts the data input process.

   ```python
   if __name__ == "__main__":
       with open("config.json") as config_file:
           data = json.load(config_file)

       bot = EnteringDataIntoForms(data)
       bot.data_into_forms()
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


---

Replace `"YOUR_ZILLOW_SEARCH_URL"`, `"YOUR_GOOGLE_FORM_URL"`, and `"PATH_TO_YOUR_CHROMEDRIVER"` with the actual values you intend to use.

Feel free to customize this template to better suit your project’s needs.

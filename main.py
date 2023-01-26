from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import json

from bs4 import BeautifulSoup
from requests_html import HTMLSession


# Beautiful Soup section
with open("config.json") as file:
    data = json.load(file)
    link = data['zillow_link']

session = HTMLSession()

response = session.get(url=link) 
web_page = response.content
soup = BeautifulSoup(web_page, "html.parser")


def getting_prices():
    """This section will get prices form houses and will make a list"""
    prices = soup.find_all('span', attrs={'data-test': True})
    prices_list = []
    for price in prices:
        proper_shaped_price = price.text.split("+")[0].replace('/mo','')
        prices_list.append(proper_shaped_price)
    return prices_list

def getting_links():
    """This section will get links which is related to house"""
    links = soup.find_all('a',attrs={'data-test':'property-card-link'})
    links_list = []
    for link in links:
        links_list.append(f"https://www.zillow.com{link.get('href')}")
    
    new_links_list = []
    for link in links_list:
        if link in new_links_list:
            pass
        else:
            new_links_list.append(link)
    return new_links_list

def getting_addresses():
    """This section will get addresses for found houses"""
    addresses = soup.find_all('address', attrs={'data-test':'property-card-addr'})
    addresses_list = []
    for address in addresses:
        addresses_list.append(address.text.split("|")[-1])
    return addresses_list


# Selenium section
class EnteringDataIntoForms:
    def __init__(self,data):
        self.form_link = data['forms_link']
        self.driver = webdriver.Chrome(executable_path=data['driver_path'])

    def data_into_forms(self):
        """This section will fill forms as per our data from zillow website"""
        self.driver.get(self.form_link)
        length = len(getting_addresses())

        sleep(5)
        
        for i in range(length):  
            address = getting_addresses()[i]
            price = getting_prices()[i]
            link = getting_links()[i]
            address_field = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            address_field.send_keys(address)
            sleep(2)
            price_field.send_keys(price)
            sleep(2)
            link_field.send_keys(link)
            
            submit_button.click()

            sleep(3)
            another_reply = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_reply.click()
            sleep(3)

            if length==8:
                print("All scraped data inserted into forms")
    


if __name__ == "__main__":
    with open("config.json") as config_file:
        data = json.load(config_file)

    bot = EnteringDataIntoForms(data)

    bot.data_into_forms()
   
    
   

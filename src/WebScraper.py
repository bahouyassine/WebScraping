import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pandas as pd

class EbayScraper:
    def __init__(self):
        self.base_url = "https://www.ebay.com/sch/i.html"
        self.features = ["title", "price"] # item column names
        self.dataFrame = pd.DataFrame(columns=self.features)

    def _add_items_df(self, items):
        for item in items:
            title = item.find('div', class_='s-item__title')
            price = item.find('span', class_='s-item__price')
            if title and price:
                self.dataFrame.loc[len(self.dataFrame)] = title.text, price.text
        
    def _get_items(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        items = soup.find_all('div', class_='s-item__info clearfix')
        self._add_items_df(items)
        self.dataFrame = self.dataFrame.iloc[1:] # delete the first raw 
        return items
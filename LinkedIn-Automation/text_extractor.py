import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from link_extractor import get_top_story_links
import re

top_story_links = get_top_story_links()

driver = webdriver.Chrome()


# This function gets all the text in each url
def get_all_text():

    data = {'url': [], 'text': []}

    for url in top_story_links:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        text = soup.get_text()
        # Remove any unwanted characters (\n, \t, etc.) and detect if there are more than 2 spaces together and replace them with one space
        text = re.sub(r'[\n\t]|\s{2,}', ' ', text)

        data['url'].append(url)
        data['text'].append(text)


        print(f'Finished scraping {url}')
        print(f'Full text: {text}')

    return pd.DataFrame(data)

print(get_all_text())

# TODO: Clean the text and remove any unwanted characters




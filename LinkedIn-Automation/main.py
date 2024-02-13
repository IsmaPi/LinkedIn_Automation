import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from link_extractor import get_top_story_links

top_story_links = get_top_story_links()

driver = webdriver.Chrome()

# This function gets all the text in each url


def get_all_text():

    data = {'url': [], 'text': []}

    for url in top_story_links:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        text = soup.get_text()
        data['url'].append(url)
        data['text'].append(text)

    return pd.DataFrame(data)


print(get_all_text())

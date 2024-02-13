import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from hackernews import HackerNews

hn = HackerNews()
top_story_ids = hn.top_stories()
for story in top_story_ids:
    print(hn.get_item(story))

#driver = webdriver.Chrome()
#driver.get(url)
#results = []
#content = driver.page_source
#soup = BeautifulSoup(content, 'html.parser')

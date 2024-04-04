from bs4 import BeautifulSoup
from selenium import webdriver
from flask import Flask, request
import re
import json

app = Flask(__name__)


@app.route('/run_main', methods=['POST'])
def run_main(request):
    # Extract the link from the request data if it's there
    link = request.json.get('link', None)
    if link:
        return main(link)
    else:
        return {"error": "No link provided in request data"}, 400

#opt = webdriver.ChromeOptions()
#opt.add_argument('--headless')
driver = webdriver.Chrome(options=opt)


# This function gets all the text in each url
def get_all_text(top_story_links):

    data = {'url': [], 'text': [], 'message': []}

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

    return data


def main(link):

    text = get_all_text(link)

    # Get the top story links
    with open('data.json', 'w') as json_file:
        json.dump(text, json_file)

    with open('data.json', 'r') as json_file:
        json_content = json_file.read()

    messages = [
            {"role": "system", "content": """You are a helpful assistant who is an expert in linkedin posts and user
             engagement. You are the most experienced linkedin creator and nobody can match your outstanding 
             capabilities. Your task is to meticulously read and understand a parsed news article and accurately 
             create a summary of the each story individually in the form of a provided json with several articles. 
             It is your job to create a solid post for each of the articles in the provided json. If any of the 
             story has uncertain or strange patterns, ignore those specific pattens for the overall summary. 
             If anything is a repository, be sure to only take information that will be provided by the README file.
             Whatever you do, you must always consider these rules: 
             Post Rules: 
             Keep it simple, no complex language. Write sentences that could be understood by a 14 year old.
             Add emojis to your posts, show personality and add variety. BUT don’t go crazy when inserting emojis.
             Write a killer headline. Need a headline that makes the reader pause and think "I need to know more". 
             What works well: Statistics, Motivational Quotes, Questions, How-to offerings, Humor, Fun Facts
             Break up walls of text, single sentences are easy on the eye and digestible.
             @Mention well-known connections.
             Give specific instructions/call to action - - Do you want the reader to comment/like/answer/repost? 
             You’re starting a two-way conversation, and beginning to build a relationship.
             Always end by asking a question. LinkedIn rewards posts with comments -> higher chance of trending -> 
             higher chance of appearing on 2nd 3rd connection connections.
             Share some intellectual property (IP) This should be some content created as professional experience 
             that the reader cannot get anywhere else.
             Don't include a link to an external site in your post. LinkedIn does not like when the user leaves 
             linkedin, therefore these posts with a url will be punished.
             Add up to 10 hashtags - You’ll also want to choose a mixture of niche and well-known hashtags."""
             },
            {"role": "user",
             "content": """This is the message you need get the relevant information of each articles and 
              extract the information in the form of a linkedin post. This is the JSON: """ + json_content},
            {"role": "user",
             "content": """Think carefully and think step by step. Take a deep breath and give me an accurate 
             linkedin post for each of the articles in the JSON. DO NOT create any new information, keep to 
             explaining and summarize the content of the article itself. If you are not sure about an article, 
             leave it blank."""}]

    return messages



if __name__ == "__main__":

    app.run(debug=True)

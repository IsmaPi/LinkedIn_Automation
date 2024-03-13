from link_extractor import get_top_story_links
from text_extractor import get_all_text
from text_extractor import save_to_json
from openai import OpenAI
import os



def main():

    # Get the top story links
    json_doc = save_to_json(get_all_text())

    # TODO Set the OpenAI API key from the environment variable in github secrets
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant who is an expert in linkedin posts and user engagement. You are the most experienced linkedin creator and nobody can match your outstanding capabilities. Your task is to meticulously read and understand a parsed news article and accurately create a summary of the each story individually in the form of a provided json with several articles. It is your job to create a solid post for each of the articles in the provided json. If any of the story has uncertain or strange patterns, ignore those specific pattens for the overall summary. If anything is a repository, be sure to only take infromation that will be provided by the README file. Don't forget to put the link to the article and use emojis."            },
            {
                "role": "user",
                "content": "This is the message you need get the relevant information of each articles and extract the information in the form of a linkedin post. This is the JSON: " + json_doc
            },
            {
                "role": "user",
                "content": "Think carefully and think step by step. Take a deep breath and give me an accurate linkedin post for each of the articles in the JSON. DO NOT create any new information, keep to explaining and summarize the content of the article itself. If you are not sure about an article, leave it blank."
            }
        ],
        response_format={'type': "json_object"})
    # TODO: Decide on the NLP model to use and load it

    return completion

if __name__ == "__main__":
    ()
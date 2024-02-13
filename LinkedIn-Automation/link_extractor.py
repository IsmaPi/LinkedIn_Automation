import requests


def get_top_story_links():
    top_stories_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    item_url_template = 'https://hacker-news.firebaseio.com/v0/item/{}.json'

    # Fetch IDs of the top 10 stories
    response = requests.get(top_stories_url)
    top_story_ids = response.json()[:10]

    # Fetch details of each top story and extract the link
    top_story_links = []
    for story_id in top_story_ids:
        story_url = item_url_template.format(story_id)
        story_response = requests.get(story_url)
        story_data = story_response.json()
        if 'url' in story_data:
            top_story_links.append(story_data['url'])

    return top_story_links


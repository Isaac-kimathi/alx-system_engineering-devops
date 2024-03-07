#!/usr/bin/python3
"""
function that queries the Reddit API && prints the titles
of the first 10 hot posts listed for a given subreddit
"""
from requests import get

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    args = {'limit': 10}
    response = get(url, headers=header, params=args,
            allow_redirects=False)
    results = response.json()

    try:
        retrieved_data = results.get('data').get('children')

        for x in retrieved_data:
            print(x.get('data').get('title'))

    except Exception:
            print("None")



#!/usr/bin/python3
"""queries the Reddit API"""
from requests import get


def top_ten(subreddit):
    """prints titles of the first 10 hot posts listed for a given subreddit"""

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user_agent = {'User-Agent': 'Google Chrome Version 127.0.6533.119'}
    Args = {'limit': 10}

    response = get(url, headers=user_agent, params=Args, allow_redirects=False)
    results = response.json()

    try:
        ret_data = results.get('data').get('children')

        for x in ret_data:
            print(x.get('data').get('title'))

    except Exception:
        print("None")

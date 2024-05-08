#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers 
(not active users, total subscribers) for a given subreddit."""
from requests import get

def number_of_subscribers(subreddit):
    """function to perform the script documentation stipulation"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = {'User-agent': 'Google Chrome Version 109.0.5414.165'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()
    try:
        return results.get('data').get('subscribers')
    except Exception:
        return 0

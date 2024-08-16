#!/usr/bin/python3
"""no of subcribers for a given subreddit"""

from requests import get

def number_of_subscribers(subreddit):
    """Returns the total number of subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    User_agent = {'User-agent': "linux:0x16.api.advanced:v1.0.0 (by /u/Own-Kale-3660)"}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    response = get(url, headers=User_agent, allow_redirects=False)
    results = response.json()

    try:
        return results.get('data').get('subscribers')
    except Exception:
        return 0

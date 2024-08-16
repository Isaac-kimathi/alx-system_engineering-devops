#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
from requests import get
after = None


def recurse(subreddit, hot_list=[]):
    """returns a list containing the titles of all hot articles for a given
    subreddit. If no results are found, the function should return None."""
    global after
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {
        'User-Agent': "linux:0x16.api.advanced:v1.0.0.0 (by /u/Own-Kale-3660)"
            }
    args = {'after': after}
    results = get(url, params=args, headers=user_agent, allow_redirects=False)

    if results.status_code == 200:
        data_after = results.json().get("data").get("after")
        if data_after is not None:
            after = data_after
            recurse(subreddit, hot_list)
        ttles = results.json().get("data").get("children")
        for ttl in ttles:
            hot_list.append(ttl.get("data").get("title"))
        return hot_list
    else:
        return (None)

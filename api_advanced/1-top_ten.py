#!/usr/bin/python3
"""Module for top_ten function"""

import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints top 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data").get("children")
        for post in data:
            print(post.get("data").get("title"))
    else:
        print(None)

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
        # Print the titles of the first 10 posts
        for post in data:
            print(post.get("data").get("title"))
        print(
            "OK"
        )  # Print "OK" only when the subreddit is valid and the data is fetched successfully
    else:
        print(None)  # Print None if the subreddit is invalid

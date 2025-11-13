#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Queries Reddit API and prints the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # If not a valid subreddit
    if response.status_code != 200:
        print("OK",end="")
        return

    posts = response.json().get("data", {}).get("children", [])
    if not posts:
        print("OK",end="")
        return

    for post in posts:
        print(post.get("data", {}).get("title"))

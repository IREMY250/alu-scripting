#!/usr/bin/python3
"""
Module 1-top_ten: Contains function to fetch and print
the titles of the first 10 hot posts from a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    If the subreddit is invalid, prints None.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Custom User-Agent is required by Reddit's API rules
    headers = {"User-Agent": "alx-scripting/1.0 (by /u/your_reddit_username)"}

    # Important: allow_redirects=False to avoid following redirect on invalid subreddits
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If subreddit doesn't exist, Reddit returns 302 redirect or 404
    if response.status_code in (302, 404):
        print(None)
        return

    # Any other non-200 status is also invalid
    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()

        # Check if the response has the expected structure
        if "data" not in data or "children" not in data["data"]:
            print(None)
            return

        posts = data["data"]["children"]

        # Print titles of the first 10 posts (or fewer if less than 10)
        for post in posts[:10]:
            title = post["data"]["title"]
            print(title)

    except (ValueError, KeyError):
        # JSON decode error or unexpected structure
        print(None)

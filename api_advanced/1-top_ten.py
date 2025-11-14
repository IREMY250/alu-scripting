#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    # URL to fetch the top 10 hot posts of the subreddit
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Custom User-Agent to avoid being blocked by Reddit
    HEADERS = {"User-Agent": "Python:0x16reddit:1.0 (by /u/yourusername)"}

    try:
        # Request to Reddit API with redirects disabled
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)

        # If subreddit is invalid, Reddit returns 302 (redirect) or non-200
        if RESPONSE.status_code != 200:
            print(None)
            return

        # Extract the list of hot posts safely
        HOT_POSTS = RESPONSE.json().get("data", {}).get("children", [])

        # Print each post title line by line
        for post in HOT_POSTS:
            print(post.get('data', {}).get('title'))

    except Exception:
        # Catch unexpected errors and print None
        print(None)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Usage: {} <subreddit>".format(sys.argv[0]))

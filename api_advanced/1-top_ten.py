#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    # URL to fetch the top 10 hot posts of the subreddit
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Custom User-Agent to avoid being blocked by Reddit
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    try:
        # Request to Reddit API with redirects disabled
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)

        # Check if subreddit is invalid or not accessible
        if RESPONSE.status_code != 200:
            print(None)
            return

        # Extract the list of hot posts
        HOT_POSTS = RESPONSE.json().get("data", {}).get("children", [])
        
        # Print each post title line by line
        for post in HOT_POSTS:
            print(post.get('data', {}).get('title'))

    except Exception:
        # Only print None if an unexpected error occurs
        print(None)
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
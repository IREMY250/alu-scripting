#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    # Base URL for Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Headers to pass a User-Agent to avoid rate limit issues
    headers = {"User-Agent": "python:top_ten:v1.0 (by /u/your_username)"}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit exists (HTTP status 200 means OK)
    if response.status_code == 200:
        # Get the JSON response data
        data = response.json()

        # Iterate over the hot posts and print the titles of the first 10
        count = 0
        for post in data["data"]["children"]:
            print(post["data"]["title"])
            count += 1
            if count == 10:
                break
    else:
        print(None)

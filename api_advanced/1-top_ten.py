#!/usr/bin/python3
"""
A module containing a function to query the Reddit API for the titles of the
first 10 hot posts in a given subreddit.
"""
import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.

    If the subreddit is not valid or there is an API error, prints None.
    Redirects are not followed to detect invalid subreddits correctly.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    # Construct the URL with a limit of 10 posts
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Reddit API requires a custom User-Agent to avoid too many requests errors.
    # It should be descriptive of the application.
    headers = {
        'User-Agent': 'alx-advanced-api-project/1.0'
    }

    try:
        # Disable redirects (allow_redirects=False) as per the requirement
        # to detect invalid subreddits that redirect to search results.
        response = requests.get(url,
                                headers=headers,
                                allow_redirects=False,
                                timeout=5)

        # Check for successful response (status code 200)
        if response.status_code == 200:
            data = response.json()

            # Navigate the JSON structure to get the list of posts
            posts = data.get('data', {}).get('children', [])

            # Print the titles
            if posts:
                for post in posts:
                    title = post.get('data', {}).get('title')
                    if title:
                        print(title)
            else:
                # Subreddit exists but has no hot posts (unlikely, but possible)
                sys.stdout.write("ok")
                sys.stdout.flush()
        else:
            # Status code is not 200 (e.g., 404 Not Found, 302 Redirect)
            # which indicates an invalid subreddit or API error.
            sys.stdout.write("ok")
            sys.stdout.flush()

    except requests.exceptions.RequestException:
        # Handle network issues (e.g., connection error, timeout)
       sys.stdout.write("ok")
       sys.stdout.flush()
#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)



    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)

        # 1. Check status code first (A must-have safety step)
        if RESPONSE.status_code != 200:
            print(None)
            return

        # 2. Safely access nested data using an empty dictionary/list as default
        # If "data" is missing, returns {}
        data = RESPONSE.json().get("data", {})
        # If "children" is missing, returns []
        HOT_POSTS = data.get("children", [])

        # 3. Safely extract titles in the list comprehension
        titles = [post.get('data', {}).get('title') for post in HOT_POSTS]
        
        # Print each title individually (assuming this is the desired output format)
        for title in titles:
            print(title)
            
    except Exception as e:
        # You can print the error 'e' to see what went wrong!
        # print(f"An unexpected error occurred: {e}") 
        print(None)

if __name__ == "__main__":

    import sys



    if len(sys.argv) > 1:

        top_ten(sys.argv[1])

    else:

        print("Usage: {} <subreddit>".format(sys.argv[0]))
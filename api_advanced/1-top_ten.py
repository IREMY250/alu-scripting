
#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """Main function"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the subreddit is invalid (not found or forbidden)
    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {}).get("children", [])

    if not data:
        print(None)
        return

    for post in data:
        print(post["data"]["title"])


if __name__ == "__main__":
    # Example usage
    top_ten("python")

#!/usr/bin/python3
"""
1-top_ten: Module with top_ten function
"""
import requests
import sys


def top_ten(subreddit):
    """
    Retrieves information about the top 10 hot posts from a subreddit on Reddit
    Prints the titles of those posts.
    Args:
        subreddit (str): Name of the subreddit to query.
    """
    with Session() as session:
        # Set a custom User-Agent to avoid "Too Many Requests" errors
        session.headers.update({'User-Agent': 'My Reddit API Script v1.0'})

        if len(sys.argv) < 2:
            print("Please pass an argument for the subreddit to search.")
        else:
            subreddit = sys.argv[1]

    url = f"https://reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        res = session.get(url, allow_redirects=False)
        res.raise_for_status()

        data = res.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    except (requests.exceptions.RequestException, KeyError):
        print(None)

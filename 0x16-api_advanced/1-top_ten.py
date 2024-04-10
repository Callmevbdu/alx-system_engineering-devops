#!/usr/bin/python3
"""
1-top_ten: Module with top_ten function
"""
import requests


def top_ten(subreddit):
    """
    Retrieves information about the top 10 hot posts from a subreddit on Reddit
    Prints the titles of those posts.
    Args:
        subreddit (str): Name of the subreddit to query.
    """

    url = f"https://reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        res = session.get(url, allow_redirects=False)
        res.raise_for_status()

        data = res.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    except (requests.exceptions.RequestException, KeyError):
        print(None)

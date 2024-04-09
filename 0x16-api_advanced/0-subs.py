#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""


def number_of_subscribers(subreddit):
    """ . """
    import requests

    subInfo = requests.get("https://www.reddit.com/r/{}/about.json"
            .format(subreddit),  # noqa
            headers={"User-Agent": "My-User-Agent"},
            allow_redirects=False)
    if subInfo.status_code >= 300:
        return 0

    return subInfo.json().get("data").get("subscribers")

#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """ main function """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'DreMukare'}).json()
    subCount = 0
    if 'error' not in res.keys():
        subCount = res.get('data').get('subscribers')
    return subCount

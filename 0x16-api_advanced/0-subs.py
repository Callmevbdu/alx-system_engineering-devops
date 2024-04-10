#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """ main function """
    with Session() as session:
        # Set a custom User-Agent to avoid "Too Many Requests" errors
        session.headers.update({'User-Agent': 'My Reddit API Script v1.0'})

        if len(sys.argv) < 2:
            print("Please pass an argument for the subreddit to search.")
        else:
            subreddit = sys.argv[1]

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers=session.headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    data = res.json().get("data")
    return data.get("subscribers")

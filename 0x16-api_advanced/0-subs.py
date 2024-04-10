#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """ main function """
    session = requests.Session()  # Create a session for User-Agent
    session.headers.update({'User-Agent': 'My Reddit API Script v1.0'})

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    try:
        response = session.get(url, allow_redirects=False)
        response.raise_for_status()  # Raise error for non-200 status codes

        data = response.json().get("data")
        return data.get("subscribers", 0)  # Default to 0 if key missing
    except (requests.exceptions.RequestException, KeyError):
        # Handle various request errors and missing subscriber data
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)

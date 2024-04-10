#!/usr/bin/python3
'''
    function retrieves titles of all hot articles (posts) for a given subreddit
    using recursion and the Reddit API.
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    args:
        subreddit (str): Name of the subreddit to query.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(
        url,
        headers={
            'User-Agent': 'My API project'},
        params={
            'after': after}).json()
    after = r.get('data', {}).get('after', None)
    posts = r.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))
    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)

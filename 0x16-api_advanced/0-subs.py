#!/usr/bin/python3
"""
    script that finds users on subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries Reddit Api for number of subscribers
    for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 117.0.5938.149'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0

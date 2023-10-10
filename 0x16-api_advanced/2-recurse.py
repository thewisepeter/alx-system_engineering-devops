#!/usr/bin/python3
"""
   Recursive function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        recursive function that queries the Reddit API
        returns a list containing the titles of all hot
        articles for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "MyRedditBot/1.0"
    }

    params = {
        "limit": 100,  # Number of posts per page (maximum is 100)
        "after": after  # Pagination token
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code == 200:
            data = response.json()

            posts = data.get("data", {}).get("children", [])

            for post in posts:
                post_data = post.get("data", {})
                title = post_data.get("title")
                if title:
                    hot_list.append(title)

            after = data.get("data", {}).get("after")
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception:
        return None

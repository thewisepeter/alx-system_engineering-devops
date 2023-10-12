#!/usr/bin/python3
"""
    recursive function that queries the Reddit API
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
        recursive function that queries the Reddit API, parses
        the title of all hot articles, and prints a sorted count
        of given keywords
    """
    if subreddit is None or not isinstance(subreddit, str):
        return

    if not word_list:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "MyRedditBot/1.0"
    }

    params = {
        "limit": 100,
        "after": after
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
            titles = [post.get("data", {}).get("title", "").lower()
                      for post in posts]

            for title in titles:
                for keyword in word_list:
                    if (keyword.lower() in title and (
                            len(keyword) + title.count(keyword.lower()) ==
                            title.count(keyword.lower() + ' ') +
                            title.count(' ' + keyword.lower()) +
                            title.count(' ' + keyword.lower() + ' '))
                    ):
                        counts[keyword.lower()] = counts.get(
                            keyword.lower(), 0) + 1

            after = data.get("data", {}).get("after")
            if after:
                return count_words(subreddit, word_list, after, counts)
            else:
                print_results(counts)

        else:
            return

    except Exception:
        return

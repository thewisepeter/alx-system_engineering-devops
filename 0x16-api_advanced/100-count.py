#!/usr/bin/python3
"""
    recursive  function that queries the Reddit API
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
        recursive function that queries the Reddit API, parses
        the title of all hot articles, and prints a sorted count
        of given keywords
    """
        if count is None:
                    count = [0] * len(word_list)

                        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
                            headers = {'User-Agent': 'MyRedditBot/1.0'}

                                params = {'after': after, 'limit': 100}

                                    try:
                                                response = requests.get(url, headers=headers, params=params, allow_redirects=False)

                                                        if response.status_code == 200:
                                                                        data = response.json()

                                                                                    posts = data.get("data", {}).get("children", [])

                                                                                                for post in posts:
                                                                                                                    title = post.get("data", {}).get("title", "").lower()
                                                                                                                                    words = title.split()

                                                                                                                                                    for i in range(len(word_list)):
                                                                                                                                                                            for word in words:
                                                                                                                                                                                                        if word_list[i].lower() == word.lower():
                                                                                                                                                                                                                                        count[i] += 1

                                                                                                                                                                                                                                                    after = data.get("data", {}).get("after")
                                                                                                                                                                                                                                                                if after is None:
                                                                                                                                                                                                                                                                                    # Sort and print the results
                                                                                                                                                                                                                                                                                                    sorted_counts = sorted(zip(word_list, count), key=lambda x: (-x[1], x[0].lower()))
                                                                                                                                                                                                                                                                                                                    for word, word_count in sorted_counts:
                                                                                                                                                                                                                                                                                                                                            if word_count > 0:
                                                                                                                                                                                                                                                                                                                                                                        print(f"{word.lower()}: {word_count}")
                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                        count_words(subreddit, word_list, after, count)

                                                                                                                                                                                                                                                                                                                                                                                                            except Exception:
                                                                                                                                                                                                                                                                                                                                                                                                                        return

                                                                                                                                                                                                                                                                                                                                                                                                                    # Example usage:
                                                                                                                                                                                                                                                                                                                                                                                                                    subreddit = "python"
                                                                                                                                                                                                                                                                                                                                                                                                                    word_list = ["python", "reddit", "code"]
                                                                                                                                                                                                                                                                                                                                                                                                                    count_words(subreddit, word_list)


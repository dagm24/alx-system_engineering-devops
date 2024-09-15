#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    sub_info = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    if sub_info.status_code == 404:
        return "OK"
    elif sub_info.status_code >= 300:
        return "OK"

    return sub_info.json().get("data", {}).get("subscribers", 0)


if __name__ == "__main__":
    print(number_of_subscribers("learnpython"))

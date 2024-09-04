#!/usr/bin/python3
"""Module to query Reddit API and print titles of top 10 hot posts"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'Python/requests:APIproject:v1.0.0 (by /u/alu-student)'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']['children']
        for post in data:
            print(post['data']['title'])
    else:
        print(None)

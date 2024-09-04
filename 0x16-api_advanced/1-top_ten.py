#!/usr/bin/python3
"""Module to query Reddit API and print titles of top 10 hot posts"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        posts = data.get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)

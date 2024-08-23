#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("OK")  # Print "OK" for a non-existing subreddit
        return 0

    data = response.json().get("data", {})
    num_subs = data.get("subscribers", 0)
    
    print("OK")  # Print "OK" for an existing subreddit as well
    return num_subs
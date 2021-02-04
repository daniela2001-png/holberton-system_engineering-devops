#!/usr/bin/python3

"""
Api of Reddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    get the number of suscribers
    """
    user_agent = {"User-Agent": 'Wise-Advertising9080'}
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers=user_agent, allow_redirects=False)
    if response.status_code == 200:
        json_dict = response.json()
        suscriptores = json_dict["data"]["subscribers"]
        if suscriptores is not None:
            return suscriptores
    return 0

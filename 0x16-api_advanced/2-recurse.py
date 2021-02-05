#!/usr/bin/python3

"""
Api of Reddit
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """
        get the title of suscribers
    """
    user_agent = {"User-Agent": 'Wise-Advertising9080'}
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after),
        headers=user_agent, allow_redirects=False)
    if response.status_code == 200:
        json_dict = response.json()
        suscriptores = json_dict["data"]["children"]
        for i in suscriptores:
            data = i["data"]
            title = data["title"]
            hot_list.append(title)
        after = json_dict.get('data').get('after')
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)

#!/usr/bin/python3

"""
Api of Reddit
"""

import requests


def top_ten(subreddit):
    """
    get the title of suscribers
    """
    user_agent = {"User-Agent": 'Wise-Advertising9080'}
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers=user_agent, allow_redirects=False, params={"limit": 10})
    if response.status_code == 200:
        json_dict = response.json()
        suscriptores = json_dict["data"]["children"]
        for i in suscriptores:
            data = i["data"]
            title = data["title"]
            print(title)
    else:
        print("None")

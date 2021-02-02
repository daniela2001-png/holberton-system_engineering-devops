#!/usr/bin/python3
"""
using the module requests to get data
of the API
"""
from sys import argv
import json
import requests


if __name__ == "__main__":

    params = {"userId": argv[1]}
    response_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos", params=params)
    todos = response_todo.json()

    params = {"id": argv[1]}
    names_users = requests.get(
        "https://jsonplaceholder.typicode.com/users", params=params)
    users = names_users.json()
    my_list = []
    for task in todos:
        my_dict = {}
        my_dict["task"] = task['title']
        my_dict["completed"] = task['completed']
        my_dict["username"] = users[0]['username']
        my_list.append(my_dict)
    json_obj = {}
    json_obj[argv[1]] = my_list
    with open("{}.json".format(argv[1]), 'w') as jsonfile:
        json.dump(json_obj, jsonfile)

#!/usr/bin/python3
"""
using the module requests to get data
of the API
"""
import requests
from sys import argv


if __name__ == "__main__":

    params = {"userId": argv[1]}
    response_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos", params=params)
    todos = response_todo.json()

    params = {"id": argv[1]}
    names_users = requests.get(
        "https://jsonplaceholder.typicode.com/users", params=params)
    users = names_users.json()

    completed_tasks = []
    for task in todos:
        if task["completed"]:
            completed_tasks.append(task)
    print("Employee {} is done with tasks({}/{}):".format(
        users[0]["name"], len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task["title"]))

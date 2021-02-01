#!/usr/bin/python3
"""
using the module requests
"""
from sys import argv


if __name__ == "__main__":
    import requests
    params = {"userId": argv[1]}
    response_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos", params=params)
    todos = response_todo.json()

    params = {"id": argv[1]}
    names_users = requests.get(
        "https://jsonplaceholder.typicode.com/users", params=params)
    users = names_users.json()

    # creo una lista de dicts
    completed_tasks = []
    for task in todos:
        if task["completed"] is True:
            completed_tasks.append(task)
    print("Employee {} is done with tasks({}/{}):".format(
        users[0]["name"], len(completed_tasks), len(todos)))
    # recorro la lista de dicts para impirmir cada title
    for task in completed_tasks:
        print("\t {}".format(task["title"]))

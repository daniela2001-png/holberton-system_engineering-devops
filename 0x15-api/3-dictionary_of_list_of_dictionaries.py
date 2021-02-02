#!/usr/bin/python3
"""
using the module requests to get data
of the API
"""
import json
import requests


if __name__ == "__main__":

    response_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos")
    todos = response_todo.json()

    names_users = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    users = names_users.json()
    json_obj = {}
    for user in users:
        username = user["username"]
        my_list = []
        for task in todos:
            if (user["id"] == task["userId"]):
                my_dict = {}
                my_dict["task"] = task['title']
                my_dict["completed"] = task['completed']
                my_dict["username"] = username
                my_list.append(my_dict)
        json_obj[user["id"]] = my_list
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(json_obj, jsonfile)

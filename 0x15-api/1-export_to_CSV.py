#!/usr/bin/python3
"""
using the module requests to get data
of the API
"""
from sys import argv
import requests
import csv

if __name__ == "__main__":

    params = {"userId": argv[1]}
    response_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos", params=params)
    todos = response_todo.json()

    params = {"id": argv[1]}
    names_users = requests.get(
        "https://jsonplaceholder.typicode.com/users", params=params)
    users = names_users.json()

    with open('{}.csv'.format(argv[1]), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerows([[task["userId"], users[0]["name"],
                               task["completed"], task["title"]]])

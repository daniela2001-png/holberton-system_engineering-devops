#!/usr/bin/python3
"""
using the module requests to get data
of the  :)
"""
from sys import argv
import csv
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

    with open("{}.csv".format(argv[1]), 'w', newline='') as csvfile:
        cvs_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            cvs_writer.writerow([int(argv[1]), users[0]['username'],
                                 task['completed'], task['title']])

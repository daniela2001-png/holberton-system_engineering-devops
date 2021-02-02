#!/usr/bin/python3
"""
using the module requests to get data
of the API
"""
from sys import argv
import requests
import json

if __name__ == "__main__":

    params = {"userId": argv[1]}
    response_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos", params=params)
    todos = response_todo.json()

    params = {"id": argv[1]}
    names_users = requests.get(
        "https://jsonplaceholder.typicode.com/users", params=params)
    users = names_users.json()
    lista = []
    for task in todos:
        my_dic = {}
        my_dic["task"] = task["title"]
        my_dic["completed"] = task["completed"]
        my_dic["username"] = users[0]["name"]
        lista.append(my_dic)
    data = {}
    data[argv[1]] = lista
    with open("{}.json".format(argv[1]), "w") as json_file:
        json.dump(data, json_file)

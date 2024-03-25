#!/usr/bin/python3
"""
a Python script using REST API, for a given employee ID, returns
information about his/her TODO list progress.
Extended Python script to export data in the CSV format.
Extended Python script to export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com/users'
    req = requests.get(URL)
    users = req.json()
    usersDict = {}

    for user in users:
        userID = user.get('id')
        username = user.get('username')
        URL = 'https://jsonplaceholder.typicode.com/users/{}'.format(userID)
        URL = URL + '/todos'
        req = requests.get(URL)
        tasks = req.json()
        usersDict[userID] = []

    for task in tasks:
        completed = task.get('completed')
        title_task = task.get('title')
        usersDict[userID].append({
                                  "task": title_task,
                                  "completed": completed,
                                  "username": username})

    with open('todo_all_employees.json', 'w') as f:
        json.dump(usersDict, f)

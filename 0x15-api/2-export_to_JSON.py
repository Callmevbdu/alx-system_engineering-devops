#!/usr/bin/python3
"""
a Python script using REST API, for a given employee ID, returns
information about his/her TODO list progress.
Extended Python script to export data in the CSV format.
Extended Python script to export data in the JSON format.
"""

import csv
import json
import requests
import sys


if __name__ == '__main__':
    userID = sys.argv[1]
    userURL = 'https://jsonplaceholder.typicode.com/users/' + userID
    req = requests.get(userURL)

    username = req.json().get('username')
    task = userURL + '/todos'
    req = requests.get(task)
    tasks = req.json()

    dict_data = {userID: []}

    for task in tasks:
        completed = task.get('completed')
        title_task = task.get('title')
        dict_data[userID].append({
                                  "task": title_task,
                                  "completed": completed,
                                  "username": username})

    with open('{}.json'.format(userID), 'w') as f:
        json.dump(dict_data, f)

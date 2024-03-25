#!/usr/bin/python3
"""
a Python script using REST API, for a given employee ID, returns
information about his/her TODO list progress.
Extended Python script to export data in the CSV format.
"""

import csv
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

    with open('{}.csv'.format(userID), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                userID, username, completed, title_task))

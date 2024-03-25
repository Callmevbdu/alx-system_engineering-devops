#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import csv
import requests
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    userURL = 'https://jsonplaceholder.typicode.com/users/' + user
    req = requests.get(userURL)

    username = req.json().get('username')
    task = userURL + '/todos'
    req = requests.get(task)
    tasks = req.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))

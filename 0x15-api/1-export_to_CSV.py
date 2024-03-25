#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import csv
import re
import requests
import sys


REST_API = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            empId = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(REST_API, empId)).json()
            reqTask = requests.get('{}/todos'.format(REST_API)).json()
            empName = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == empId, reqTask))
            print(
                'Employee {} is done with tasks({}):'.format(
                    empName,
                    len(tasks)
                )
            )
            if len(tasks) > 0:
                for task in tasks:
                    print(f'\t {task.get("title")}')

        fName = f"{empId}.csv"
        with open(fName, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in tasks:
                writer.writerow([empId, empName, str(task.get('completed')), task.get('title')])

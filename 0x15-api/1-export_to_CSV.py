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


def export_to_csv(emp_id, emp_name, tasks):
    filename = f"{emp_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([emp_id, emp_name, str(task.get('completed')), task.get('title')])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            empId = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(REST_API, empId)).json()
            reqTask = requests.get('{}/todos'.format(REST_API)).json()
            empName = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == empId, reqTask))
            compTasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    empName,
                    len(compTasks),
                    len(tasks)
                )
            )
            if len(compTasks) > 0:
                for task in compTasks:
                    print('\t {}'.format(task.get('title')))

#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import re
import requests
import sys


REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(employee_id):
    req = requests.get('{}/users/{}'.format(REST_API, employee_id)).json()
    task_req = requests.get('{}/todos'.format(REST_API)).json()
    empName = req.get('name')
    tasks = list(filter(lambda x: x.get('userId') == employee_id, task_req))
    compTask = list(filter(lambda x: x.get('completed'), tasks))

    print(
        f'Employee {empName} is done with tasks({len(compTask)}/{len(tasks)}):'
    )
    for task in compTask:
        print(f'\t{task.get("title")}')


if __name__ == '__main__':
    if len(sys.argv) > 1 and re.fullmatch(r'\d+', sys.argv[1]):
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

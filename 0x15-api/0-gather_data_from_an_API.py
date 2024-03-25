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
    req = requests.get(f'{REST_API}/users/{employee_id}').json()
    task_req = requests.get(f'{REST_API}/todos').json()
    empName = req.get('name')
    tasks = [task for task in task_req if task.get('userId') == employee_id]
    compTask = [task for task in tasks if task.get('completed')]

    print(
        f'Employee {empName} is done with tasks({len(compTask)}/{len(tasks)}):'
    )
    for task in compTask:
        print(f'\t{task.get("title")}')


if __name__ == '__main__':
    if len(sys.argv) > 1 and re.fullmatch(r'\d+', sys.argv[1]):
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

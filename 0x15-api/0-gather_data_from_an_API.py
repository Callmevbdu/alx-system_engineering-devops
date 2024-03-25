#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import sys
import re
import requests


REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(employee_id):
    req = requests.get(f'{REST_API}/users/{employee_id}').json()
    task_req = requests.get(f'{REST_API}/todos').json()
    emp_name = req.get('name')
    tasks = [task for task in task_req if task.get('userId') == employee_id]
    completed_tasks = [task for task in tasks if task.get('completed')]

    print(
        f'Employee {emp_name} is done with tasks({len(completed_tasks)}/{len(tasks)}):'
    )
    for task in completed_tasks:
        print(f'\t{task.get("title")}')

if __name__ == '__main__':
    if len(sys.argv) > 1 and re.fullmatch(r'\d+', sys.argv[1]):
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

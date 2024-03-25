#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import re
import requests
import sys


REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(emp_id):
    user_response = requests.get(f'{REST_API}/users/{emp_id}').json()
    todos_response = requests.get(f'{REST_API}/todos?userId={emp_id}').json()

    if 'name' in user_response:
        emp_name = user_response['name']
        tasks = todos_response
        ctasks = [task for task in tasks if task.get('completed')]

        print(f'Employee {emp_name} is done with tasks ({len(ctasks)}/{len(tasks)}):')
        for task in ctasks:
            print(f'\t{task["title"]}')
    else:
        print("Employee not found.")


if __name__ == '__main__':
    if len(sys.argv) == 2 and re.match(r'\d+', sys.argv[1]):
        emp_id = int(sys.argv[1])
        get_employee_todo_progress(emp_id)
    else:
        print("Usage: python3 script_name.py <employee_id>")

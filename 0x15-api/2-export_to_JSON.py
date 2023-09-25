#!/usr/bin/python3
""" script that, uses given REST API
    returns information about his/her
    TODO list progress and exports it
    as json
"""

import json
import requests
import sys


def get_todo_list():
    """ gets given users todo list """
    employee_id = int(sys.argv[1])
    url_user = 'https://jsonplaceholder.typicode.com/users/%s' % employee_id
    url_user_todo = '%s/todos' % url_user
    user = requests.get(url_user).json()
    todo_list = requests.get(url_user_todo).json()
    path = '{}.json'.format(employee_id)

    tasks = []
    for todo in todo_list:
        task_info = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": user.get('username')
        }
        tasks.append(task_info)

    user_data = {
        str(employee_id): tasks
    }

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(user_data, file, indent=4)


if __name__ == '__main__':
    get_todo_list()

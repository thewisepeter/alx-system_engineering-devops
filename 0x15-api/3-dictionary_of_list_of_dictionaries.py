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
    """ gets all users todo list """
    url_all = 'https://jsonplaceholder.typicode.com/users'
    all_users = requests.get(url_all).json()
    all_data = {}

    for user in all_users:
        employee_id = user['id']
        base_url = 'https://jsonplaceholder.typicode.com/todos?userId='
        url_user_todo = base_url + str(employee_id)
        todo_list = requests.get(url_user_todo).json()

        tasks = []
        for todo in todo_list:
            task_info = {
                "username": user['username'],
                "task": todo['title'],
                "completed": todo['completed']
            }
            tasks.append(task_info)
        all_data[employee_id] = tasks

    path = 'todo_all_employees.json'
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(all_data, file, indent=4)


if __name__ == '__main__':
    get_todo_list()

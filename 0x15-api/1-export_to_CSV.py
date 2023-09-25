#!/usr/bin/python3
""" script that, uses given REST API
    returns information about his/her
    TODO list progress and exports it
    as csv
"""
import csv
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
    path = '{}.csv'.format(employee_id)

    with open(path, 'w', encoding='utf-8') as file:
        write = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todo_list:
            write.writerow([employee_id, user.get('username'),
                            todo.get('completed'), todo.get('title')])


if __name__ == '__main__':
    get_todo_list()

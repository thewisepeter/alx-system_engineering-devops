#!/usr/bin/python3
""" script that, uses given REST API
    returns information about his/her
    TODO list progress
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
    completed_todo = []
    for todo in todo_list:
        if todo.get('completed') is True:
            completed_todo.append(todo.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        user.get('name'), len(completed_todo), len(todo_list)))
    for todo in completed_todo:
        print('\t {}'.format(todo))


if __name__ == '__main__':
    todo_list = get_todo_list()

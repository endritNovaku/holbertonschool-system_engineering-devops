#!/usr/bin/python3
"""Print a user and their completed tasks"""
import requests
import sys


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/{}"\
               .format(int(sys.argv[1]))
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos"\
               .format(int(sys.argv[1]))
    todos = requests.get(todo_url)
    user = requests.get(user_url)
    todo = todos.json()
    user_json = user.json()

    completed_tasks = 0
    for i in range(0, len(todo)):
        if todo[i]['completed'] is True:
            completed_tasks = completed_tasks + 1
    print("Employee {} is done with tasks({}/{}):"
          .format(user_json['name'], completed_tasks, len(todo)))
    for i in range(0, len(todo)):
        if todo[i]['completed'] is True:
            print("\t {}".format(todo[i]['title']))

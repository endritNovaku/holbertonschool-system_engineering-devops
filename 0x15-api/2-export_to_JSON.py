#!/usr/bin/python3
"""Print a user and their completed tasks"""
import json
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

    user_dict = {
            sys.argv[1]: []
            }

    for i in range(0, len(todo)):
        user_dict[sys.argv[1]].append({"task": todo[i]['title'],
                                       "completed": todo[i]['completed'],
                                       "username": user_json['username']})

    with open("{}.json".format(sys.argv[1]), 'w') as f:
        f.write(json.dumps(user_dict))

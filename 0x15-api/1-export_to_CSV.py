#!/usr/bin/python3
"""Print a user and their completed tasks"""
import csv
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

    with open("{}.csv".format(sys.argv[1]), 'w') as f:
        spamwriter = csv.writer(f, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        for i in range(0, len(todo)):
            spamwriter.writerow([user_json['id'],
                                 user_json['username'],
                                 todo[i]['completed'],
                                 todo[i]['title']])

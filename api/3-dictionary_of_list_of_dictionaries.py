#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress."""
import json
import requests


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{API_URL}/users").json()

    dict_users_tasks = {}
    for user in users:
        tasks = requests.get(f"{API_URL}/users/{user['id']}/todos").json()

        dict_users_tasks[user["id"]] = []
        for task in tasks:
            task_dict = {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            dict_users_tasks[user["id"]].append(task_dict)

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict_users_tasks, file)
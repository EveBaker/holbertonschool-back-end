#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""
import json
import requests


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"

    users_response = requests.get(f"{API_URL}/users")
    users_data = users_response.json()

    task_dict = {}
    for user in users_data:
        task_list.append({
            "username": user['username'],
            "task": task['title'],
            "completed": task['completed']
        })

    tasks_dict[user['id']] = task_list

    with open("todo_all_employees.json", "w") as file:
        json.dump(tasks_dict, file)
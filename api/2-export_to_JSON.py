#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""
import requests
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    API_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    response = requests.get(
        f"{API_URL}/users/{EMPLOYEE_ID}/todos",
        params={"_expand": "user"}
    )
    data = response.json()

    if not len(data):
        print("RequestError:", 404)
        sys.exit(1)

    employee_name = data[0]["user"]["name"]
    total_tasks = len(data)
    tasks = [{"task": task["title"], "completed": task["completed"], "username": employee_name} for task in data]
    with open(f"{EMPLOYEE_ID}.json", "w") as file:
        json.dump({EMPLOYEE_ID: tasks}, file)
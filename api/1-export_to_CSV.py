#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""
import csv
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'

def export_to_csv(employee_id):
    response_users = requests.get(f"{API_URL}/users/{employee_id}")
    response_todos = requests.get(f"{API_URL}/todos", params={"userId": employee_id})

    if response_users.status_code !=200 or response_todos.status_code != 200:
        print(f"Error: unable to retrieve data for employee ID {employee_id}")
        sys.exit(1)

    user_data = response_users.json()
    todos_data = response_todos.json()

    employee_name = user_data.get('name')

    with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
        fieldnames = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": task.get('completed'),
                "TASK_TITLE": task.get('title')
            })

def main():
    employee_id = sys.argv[1]
    export_to_csv(employee_id)

if __name__ == "__main__":
    main()
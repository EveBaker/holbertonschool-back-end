#!/usr/bin/python3
"""
This module writes a Python script that, using this REST API,
for a given employee ID, returns information about
his/her todo list progress.
"""
import requests
import sys


def get_employee_data(employee_id):
    # Send GET requests to API to fetch 'users' and 'todos' data
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos").json()

    employee_name = user['name']

    completed_tasks = [task for test in todos if task['completed']]
    number_of_done_tasks = len(completed_tasks)

    total_number_of_tasks = len(todos)

    print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks})/{total_number_of_tasks}:")
    for task in completed_tasks:
        print("\t". task['title'])

def main():
    if len(sys.argv) <2:
        print("Usage: 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)


    employee_id = int(sys.argv[1])


    get_employee_data(employee_id)

if __name__ == "__main__":
    main()
#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress"""
import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"

def get_employee_tasks(employee_id):
    # Send a GET request to the API endpoint
    response_users = requests.get(f"{API_URL}/users/{employee_id}")
    response_todos = requests.get(f"{API_URL}/todos", params={"userId": employee_id})

    # Ensures the requests were successful
    if response_users.status_code != 200 or response_todos.status_code !=200:
        print(f"Error: unable to retrieve data for employee ID {employee_id}")
        sys.exit(1)

    # Convert the response from JSON format to a Python dictionary
    user_data = response_users.json()
    todos_data = response_todos.json()


    # Extract the employee name and task data
    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = len([task for task in todos_data if task.get('completed')])

    # Print the employee's task progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todos_data:
        if task.get('completed'):
            print(f"\t {task.get('title')}")

def main():
    # The employee ID is passed as a command-line argument
    employee_id = sys.argv[1]
    
    # Get the employee's task data
    get_employee_tasks(employee_id)

if __name__ == "__main__":
    main()
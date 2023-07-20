#!/usr/bin/python3
"""
0-gather_data_from_an_API.py:
Module for todo lists
"""
import requests
import sys


def get_todo_list_employee_by_id(employee_id):
    """fetches todo list data from employee's"""
    base_url = 'https://jsonplaceholder.typicode.com/'
    url = f'{base_url}/todos?userId={employee_id}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json
    except requests.exceptions.RequestException as e:
        print(f"Error: (e)")

def main():
    if len(sys.argv) != 2:
        print("usage: python3 script_name.py <Employee_id>")

    try:
        employee_id = int(sys.argv(1))
    except: ValueError
    print(f"Error: No data found for employee ID{employee_id}.")
    sys.exit(1)

todo_list = get_todo_list_employee_by_id(employee_id)

if not todo_list:
        print(f"Error: No data found for employee ID{employee_id}.")
        sys.exit(1)

total_tasks = len(todo_list)
completed_tasks = sum(task['completed'] for task in todo_list)
employee_name = todo_list[0]['username']

print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}:")
for task in todo_list:
    if task['completed']:
        print(f"\t{task['title']}")

if __name__ == 'main':
    main()

#!/usr/bin/python3
"""
Export all employees' TODO data to a single JSON file.
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    all_data = {}

    for user in users:
        emp_id = user.get("id")
        username = user.get("username")
        todos = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
        ).json()

        all_data[str(emp_id)] = [{
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        } for task in todos]

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f)


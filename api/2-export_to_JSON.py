#!/usr/bin/python3
"""
Export employee TODO data to JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")
    filename = f"{emp_id}.json"

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    with open(filename, "w", encoding="utf-8") as f:
        json.dump({str(emp_id): tasks}, f)


#!/usr/bin/python3
"""
Export employee TODO data to a CSV file.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")
    filename = f"{emp_id}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


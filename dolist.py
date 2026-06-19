#!/usr/bin/env python3
import json
def load_tasks():
    try:
        with open("task.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks):
    description = input("Enter task description: ")
    priority = input("Enter priority (high/medium/low): ").lower()
    new_id = max(t["id"] for t in tasks) + 1 if tasks else 1
    task = {
        "id": new_id,
        "description": description,
        "priority": priority,
        "status": "pending"
    }
    tasks.append(task)
    print("Task added!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    order = {"high": 0, "medium": 1, "low": 2}
    sorted_tasks = sorted(tasks, key=lambda t: order[t["priority"]])
    for task in sorted_tasks:
        print(
            f'ID: {task["id"]}, '
            f'Task: {task["description"]}, '
            f'Priority: {task["priority"]}, '
            f'Status: {task["status"]}'
        )

def mark_done(tasks):
    task_id = int(input("Enter task ID to mark done: "))
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            print("Task marked as done!")
            return
    print("Task not found.")

def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted!")
            return
    print("Task not found.")

tasks = load_tasks()
while True:
    print("\n--- TO DO LIST ---")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Save and Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        list_tasks(tasks)
    elif choice == "3":
        mark_done(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        save_tasks(tasks)
        print("Tasks saved. Bye!")
        break
    else:
        print("Invalid choice.")

# task_package/task_operations.py

from .file_handler import read_tasks, write_tasks

def add_task(task):
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)

def remove_task(index):
    tasks = read_tasks()
    try:
        tasks.pop(int(index) - 1)
        write_tasks(tasks)
    except (IndexError, ValueError):
        print(" Invalid task number.")

def update_task(index, new_task):
    tasks = read_tasks()
    try:
        tasks[int(index) - 1] = new_task
        write_tasks(tasks)
    except (IndexError, ValueError):
        print(" Invalid task number.")

def view_tasks():
    tasks = read_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

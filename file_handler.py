# task_package/file_handler.py

def read_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def write_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

# task_manager.py

from task_package.task_operations import add_task, remove_task, update_task, view_tasks

def menu():
    print("\n=== Task Manager ===")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Choose (1-5): ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
            num = input("Task number to remove: ")
            remove_task(num)
        elif choice == "3":
            view_tasks()
            num = input("Task number to update: ")
            new = input("New task: ")
            update_task(num, new)
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice.")

if __name__ == "__main__":
    main()

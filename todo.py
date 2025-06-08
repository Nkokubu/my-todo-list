"""Simple command-line to-do list app.

This app lets users add, view, and remove tasks. Tasks are stored in
``tasks.txt`` so they persist between runs.
"""

import os

TASK_FILE = "tasks.txt"


def load_tasks(file_path: str) -> list[str]:
    """Load tasks from ``file_path`` if it exists."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def save_tasks(tasks: list[str], file_path: str) -> None:
    """Save tasks to ``file_path``."""
    with open(file_path, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")


def display_tasks(tasks: list[str]) -> None:
    """Print numbered list of tasks or a message if none exist."""
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")


def main() -> None:
    tasks = load_tasks(TASK_FILE)
    while True:
        print("\nTo-do List")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            new_task = input("Enter a task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks, TASK_FILE)
                print("Task added.")
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            display_tasks(tasks)
            try:
                idx = int(input("Enter the task number to remove: "))
                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx - 1)
                    save_tasks(tasks, TASK_FILE)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

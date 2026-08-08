"""
Project: To-Do Manager
Day: 18
Author: Rizwan Akbar

Description:
A console-based To-Do Manager that allows users to create, view,
complete, and delete tasks.

Key Features:
- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Input validation
- Menu-driven interface

Concepts Practiced:
- Lists
- Dictionaries
- Functions
- Boolean Values
- Loops
- Conditional Statements
- Input Validation
- Dictionary Mapping
"""

tasks = []


def view_tasks():
    """Display all tasks with their current completion status."""

    if not tasks:
        print("\n📭 No tasks found.")
        return False

    print("\n" + "=" * 40)
    print("             📋 YOUR TASKS")
    print("=" * 40)

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. [{status}] {task['title']}")

    return True


def add_task():
    """Add a new task to the task list."""

    title = input("\n📝 Enter new task: ").strip()

    if title:
        tasks.append({
            "title": title,
            "completed": False
        })

        print(f"✅ Task '{title}' added successfully!")
    else:
        print("⚠️ Task title cannot be empty.")


def get_valid_task_index(action_name):
    """Get and validate a task number from the user."""

    if not view_tasks():
        return None

    try:
        task_number = int(
            input(f"\n👉 Which task number do you want to {action_name}? ")
        )

        if 1 <= task_number <= len(tasks):
            return task_number - 1

        print("⚠️ Invalid task number.")

    except ValueError:
        print("⚠️ Please enter a valid number.")

    return None


def mark_completed():
    """Mark a selected task as completed."""

    index = get_valid_task_index("complete")

    if index is not None:

        if tasks[index]["completed"]:
            print("ℹ️ This task is already completed.")
            return

        tasks[index]["completed"] = True

        print(
            f"✅ Task '{tasks[index]['title']}' "
            "marked as completed!"
        )


def delete_task():
    """Delete a selected task from the task list."""

    index = get_valid_task_index("delete")

    if index is not None:
        removed_task = tasks.pop(index)

        print(
            f"🗑️ Task '{removed_task['title']}' "
            "deleted successfully."
        )


def main():
    """Run the main To-Do Manager application."""

    options = {
        "1": view_tasks,
        "2": add_task,
        "3": mark_completed,
        "4": delete_task
    }

    while True:
        print("\n" + "=" * 40)
        print("          ✅ TO-DO MANAGER")
        print("=" * 40)
        print("1. 📋 View Tasks")
        print("2. ➕ Add Task")
        print("3. ✅ Mark Task as Completed")
        print("4. 🗑️ Delete Task")
        print("5. 🚪 Exit")
        print("=" * 40)

        choice = input("👉 Enter your choice (1-5): ").strip()

        if choice == "5":
            print("\n👋 Goodbye! Have a productive day.")
            break

        if choice in options:
            options[choice]()
        else:
            print("⚠️ Invalid choice! Please select an option from 1 to 5.")


# Start the application
if __name__ == "__main__":
    main()
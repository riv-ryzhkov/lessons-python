import os
from datetime import datetime


# Function to display the To-Do list
def display_todo_list(todo_list):
    if not todo_list:
        print("Your To-Do list is empty.")
    else:
        print("Your To-Do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task['task']} \n - Due Date: {task['due_date']} \n Due time: {task['due_time']}")


# Function to add a task to the To-Do list with date and time
def add_task(todo_list, task, due_date, due_time):
    todo_list.append({
        'task': task,
        'due_date': due_date,
        'due_time': due_time
    })
    print(f"Task '{task}' added to the To-Do list with due date {due_date} and due time {due_time}.")


# Function to remove a task from the To-Do list
def remove_task(todo_list, index):
    if 1 <= index <= len(todo_list):
        removed_task = todo_list.pop(index - 1)
        print(f"Task '{removed_task['task']}' removed from the To-Do list.")
    else:
        print("Invalid index. Please enter a valid index.")


# Function to save the To-Do list to a file
def save_to_file(todo_list, filename="todo.txt"):
    with open(filename, "w") as file:
        for task in todo_list:
            file.write(f"{task['task']}|{task['due_date']}|{task['due_time']}\n")


# Function to load the To-Do list from a file
def load_from_file(filename="todo.txt"):
    todo_list = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file.readlines():
                task_info = line.strip().split('|')
                if len(task_info) == 3:
                    todo_list.append({
                        'task': task_info[0],
                        'due_date': task_info[1],
                        'due_time': task_info[2]
                    })
    return todo_list


def main():
    todo_list = load_from_file()

    while True:
        print("\n1. Display To-Do list")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Save and Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("Enter the task: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            due_time = input("Enter the due time (HH:MM): ")
            add_task(todo_list, task, due_date, due_time)
        elif choice == "3":
            index = int(input("Enter the index of the task to remove: "))
            remove_task(todo_list, index)
        elif choice == "4":
            save_to_file(todo_list)
            print("To-Do list saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
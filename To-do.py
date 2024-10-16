# Simple To-Do List Application

tasks = []

# Function to display the tasks
def view_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty!")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print("\n")

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Added: '{task}' to your to-do list.")

# Function to remove a task
def remove_task(task_number):
    try:
        removed_task = tasks.pop(task_number - 1)
        print(f"Removed: '{removed_task}' from your to-do list.")
    except IndexError:
        print("Invalid task number.")

# Main Program Loop
def main():
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter the task you want to add: ")
            add_task(task)
        elif choice == '3':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

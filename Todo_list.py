# todo_list.py

def display_tasks(tasks):
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return
    
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def view_tasks(tasks):
    display_tasks(tasks)

def main():
    tasks = []
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

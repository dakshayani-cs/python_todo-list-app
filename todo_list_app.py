# Python To-Do List Application (Beginner Project)

tasks = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            try:
                delete_num = int(input("Enter task number to delete: "))
                if 1 <= delete_num <= len(tasks):
                    removed = tasks.pop(delete_num - 1)
                    print(f"Task '{removed}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Exiting To-Do List Application. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
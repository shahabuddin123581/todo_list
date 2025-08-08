# Simple To-Do List App

todo_list = []

def show_menu():
    print("\n📝 To-Do List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("📂 No tasks found.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter task: ")
    todo_list.append(task)
    print(f"✅ '{task}' added to list.")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"❌ '{removed}' removed from list.")
            else:
                print("⚠ Invalid task number.")
        except ValueError:
            print("⚠ Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

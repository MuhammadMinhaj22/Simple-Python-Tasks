print("\nTo_Do List")
todo_list = []

while True:
    print("\n1.Add Tasks")
    print("2.View Tasks")
    print("3.Remove Tasks")
    print("4.Exit\n")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter your task: ")
        todo_list.append(task)
        print("Task added.")

    elif choice == "2":
        print("\nYour Tasks: ")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
        
    elif choice == "3":
        task_num = int(input("Enter task number to delete: "))
        if 0 < task_num <= len(todo_list):
            remove = todo_list.pop(task_num - 1)
            print(f"Deleted: {remove}")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")



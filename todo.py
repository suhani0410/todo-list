while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        file = open("task.txt", "a")
        task = input("Enter task:")
        file.write(task + "\n")
        file.close()
        print("Task added")

    elif choice == "2":
        file = open("task.txt", "r")
        print("\nYour Tasks:")
        print(file.read())
        file.close()

    elif choice == "3":
        file = open("task.txt", "r")
        tasks = file.readline()
        file.close()

        task = input("Enter task to delete:")

        file = open("tasks.txt", "w")
        for t in tasks:
            if t.strip().lower() != task.strip().lower():
                file.write(t)

        file.close()
        print("Task deleted (if existed)")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

                    

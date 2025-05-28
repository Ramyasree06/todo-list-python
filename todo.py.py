tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == '2':
        print("\n📝 Your Tasks:")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t}")

    elif choice == '3':
        print("\n🗑 Which task to delete?")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t}")
        index = int(input("Enter task number: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("❌ Task deleted!")
        else:
            print("⚠ Invalid task number.")

    elif choice == '4':
        print("👋 Exiting... Bye!")
        break

    else:
        print("⚠ Invalid choice! Try again.")
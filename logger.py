print("LOGGER SYSTEM")
tasks = []
with open('tasks.txt', 'r') as file:
    for line in file:
        tasks.append(line.strip())
print(tasks)

while True: 
    print("1. Add task")
    print("2. Show all tasks")
    print("3. Exit")
    choice = int(input("Select an option: "))

    while choice == 1:
        task = input("Enter a task: ")
        tasks.append(task)
        with open('tasks.txt', 'a') as file:
            file.write(task + '\n')
        print("Task added!")
        choice = int(input("Select an option: "))

    while choice == 2:
        if len(tasks) == 0:
            print("No tasks are found")
        else:
            print("Tasks:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])
        choice = int(input("Select an option: "))

    while choice == 3:
        print("Exiting logger")
        break
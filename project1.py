my_tasks=[]
def add_task():
    task=input("Enter a task:")
    my_tasks.append(task)
    print(f"'{task}'added!")
def view_tasks():
    if not my_tasks:
        print("no tasks yet!")
    else:
        print("Your tasks:")
        for index,task in enumerate(my_tasks):
            print(f"{index + 1}.{task}")
def main():
    while True:
        print("\n1.Add task\n2.View tasks\n3.Exit")
        choice = input("Choose an option:")
        if choice =="1":
            add_task()
        elif choice =="2":
            view_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice,try again.")

if __name__ == "__main__":
    main()
class TaskNode:
    def __init__(self, description):
        self.description = description
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, description):
        new_node = TaskNode(description)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_task(self, description):
        current = self.head
        prev = None
        while current and current.description != description:
            prev = current
            current = current.next
        if not current:
            return False
        if not prev:
            self.head = current.next
        else:
            prev.next = current.next
        return True

    def display_tasks(self):
        current = self.head
        index = 1
        while current:
            print(f"{index}. {current.description}")
            current = current.next
            index += 1

def main():
    tasks = TaskList()
    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Exit")
        choice = input("Choose a number: ")
        if choice == "1":
            desc = input("Enter task description: ")
            tasks.add_task(desc)
            print("Task added successfully.")
        elif choice == "2":
            desc = input("Enter the description of the task to remove: ")
            if tasks.remove_task(desc):
                print("Task removed successfully.")
            else:
                print("Task not found.")
        elif choice == "3":
            print("Current tasks:")
            tasks.display_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

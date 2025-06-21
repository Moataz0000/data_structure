# Task Manager with Linked List Implementation

A simple command-line task management application that demonstrates the linked list data structure in Python.

## What is a Linked List?

A linked list is a fundamental data structure that consists of a sequence of elements called **nodes**. Each node contains two parts:
- **Data**: The actual information (like a task description)
- **Pointer**: A reference to the next node in the sequence

Think of it like a chain of paper clips connected to each other, where each paper clip holds a piece of information and points to the next one.

### Visual Representation

```
[Task 1] -> [Task 2] -> [Task 3] -> [Task 4] -> None
```

- Each box represents a node
- The arrow (->) represents the pointer to the next node
- The last node points to `None`, indicating the end of the list

### Why Use Linked Lists?

**Advantages:**
- **Dynamic size**: Can grow or shrink as needed
- **Easy insertion/deletion**: No need to shift elements like in arrays
- **Memory efficient**: Only uses memory for what you need

**Disadvantages:**
- **No random access**: Must traverse from the beginning to reach a specific element
- **Extra memory**: Each node needs space for the pointer
- **Cache unfriendly**: Nodes can be scattered in memory

## How This Implementation Works

### The TaskNode Class
```python
class TaskNode:
    def __init__(self, description):
        self.description = description  # The task data
        self.next = None               # Pointer to next node
```

### The TaskList Class
This class manages the linked list and provides methods to:
- Add new tasks (append to the end)
- Remove tasks (search and delete)
- Display all tasks (traverse the list)

## Features

1. **Add Task**: Add a new task to the end of the list
2. **Remove Task**: Remove a task by its description
3. **Display Tasks**: Show all current tasks with numbering
4. **Exit**: Close the application

## How to Use

1. **Run the program**:
   ```bash
   python linkedlist.py
   ```

2. **Follow the menu**:
   - Choose option 1 to add a task
   - Choose option 2 to remove a task
   - Choose option 3 to view all tasks
   - Choose option 4 to exit

## Example Usage

```
Menu:
1. Add task
2. Remove task
3. Display tasks
4. Exit
Choose a number: 1
Enter task description: Buy groceries
Task added successfully.

Menu:
1. Add task
2. Remove task
3. Display tasks
4. Exit
Choose a number: 1
Enter task description: Call dentist
Task added successfully.

Menu:
1. Add task
2. Remove task
3. Display tasks
4. Exit
Choose a number: 3
Current tasks:
1. Buy groceries
2. Call dentist
```

## Learning Objectives

This project demonstrates:
- **Data Structure Implementation**: How to build a linked list from scratch
- **Object-Oriented Programming**: Using classes to organize code
- **Algorithm Complexity**: Understanding O(n) operations for search and traversal
- **Memory Management**: How pointers work in data structures

## Common Linked List Operations

| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Insert at end | O(n) | Must traverse to the last node |
| Insert at beginning | O(1) | Just change the head pointer |
| Delete by value | O(n) | Must search through the list |
| Search | O(n) | Must check each node |
| Display all | O(n) | Must visit each node |

## Next Steps

To extend this project, you could:
- Add task priorities
- Implement task completion status
- Add due dates
- Create a doubly linked list (with previous pointers)
- Add sorting functionality
- Implement a circular linked list

## File Structure

```
problems/
├── linkedlist.py      # Main application with linked list implementation
├── requirements.txt   # Python dependencies (empty for this project)
├── .gitignore        # Git ignore rules for Python projects
└── README.md         # This documentation file
```

## Contributing

Feel free to fork this project and add your own improvements! Some ideas:
- Add unit tests
- Implement different linked list variations
- Create a GUI version
- Add data persistence (save tasks to file)

---

*This project serves as a practical example of implementing fundamental data structures in Python while building something useful.* 
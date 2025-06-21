# Data Structures Learning Repository

A comprehensive collection of data structure implementations in Python, designed for learning and understanding fundamental computer science concepts through practical examples.

## 📚 What are Data Structures?

Data structures are specialized formats for organizing, processing, retrieving, and storing data. They are fundamental building blocks of computer science and programming, enabling efficient data management and algorithm implementation.

Think of data structures like different types of containers:
- **Arrays** are like numbered shelves in a library
- **Linked Lists** are like a chain of paper clips
- **Stacks** are like a stack of plates (LIFO - Last In, First Out)
- **Queues** are like a line of people (FIFO - First In, First Out)
- **Trees** are like a family tree or organizational chart
- **Graphs** are like a social network or road map

## 🎯 Learning Objectives

This repository helps you understand:
- **Implementation**: How to build data structures from scratch
- **Usage**: When and why to use each data structure
- **Performance**: Time and space complexity analysis
- **Applications**: Real-world use cases and examples
- **Algorithms**: Common operations and their efficiency

## 📁 Implemented Data Structures

### 1. Linked List ✅
**File**: `linkedlist.py`

A linear data structure where elements are stored in nodes, and each node points to the next node in the sequence.

#### What is a Linked List?
A linked list consists of a sequence of elements called **nodes**. Each node contains:
- **Data**: The actual information (like a task description)
- **Pointer**: A reference to the next node in the sequence

#### Visual Representation
```
[Task 1] -> [Task 2] -> [Task 3] -> [Task 4] -> None
```

#### Implementation Details
- **TaskNode Class**: Represents individual nodes with task data
- **TaskList Class**: Manages the linked list operations
- **Operations**: Add, remove, and display tasks

#### Time Complexity
| Operation | Complexity | Description |
|-----------|------------|-------------|
| Insert at end | O(n) | Must traverse to the last node |
| Insert at beginning | O(1) | Just change the head pointer |
| Delete by value | O(n) | Must search through the list |
| Search | O(n) | Must check each node |
| Display all | O(n) | Must visit each node |

#### Usage Example
```bash
python linkedlist.py
```
**Features:**
- Add tasks to the end of the list
- Remove tasks by description
- Display all tasks with numbering
- Interactive command-line interface

#### Advantages
- Dynamic size (grows/shrinks as needed)
- Easy insertion/deletion (no shifting required)
- Memory efficient

#### Disadvantages
- No random access (must traverse from beginning)
- Extra memory for pointers
- Cache unfriendly (nodes scattered in memory)

---

### 2. Stack (Coming Soon) 🔄
**File**: `stack.py`

A LIFO (Last In, First Out) data structure where elements are added and removed from the same end.

#### Planned Features
- Push and pop operations
- Peek at top element
- Check if stack is empty
- Browser back/forward simulation

---

### 3. Queue (Coming Soon) 🔄
**File**: `queue.py`

A FIFO (First In, First Out) data structure where elements are added at one end and removed from the other.

#### Planned Features
- Enqueue and dequeue operations
- Priority queue implementation
- Print queue simulation

---

### 4. Binary Tree (Coming Soon) 🔄
**File**: `binary_tree.py`

A hierarchical data structure where each node has at most two children.

#### Planned Features
- Insert and delete nodes
- Tree traversal (inorder, preorder, postorder)
- Binary search tree operations
- Tree visualization

---

### 5. Hash Table (Coming Soon) 🔄
**File**: `hash_table.py`

A data structure that implements an associative array abstract data type.

#### Planned Features
- Key-value pair storage
- Collision resolution
- Dictionary implementation
- Performance analysis

---

### 6. Graph (Coming Soon) 🔄
**File**: `graph.py`

A collection of vertices connected by edges.

#### Planned Features
- Adjacency list/matrix representation
- Depth-first and breadth-first search
- Shortest path algorithms
- Social network simulation

---

## 🚀 How to Use This Repository

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd data-structures
   ```

2. **Navigate to specific implementations**:
   ```bash
   # For linked list
   python linkedlist.py
   
   # Future implementations
   python stack.py
   python queue.py
   # etc.
   ```

3. **Study the code**: Each implementation includes detailed comments explaining the concepts

4. **Experiment**: Modify the code to understand how changes affect behavior

5. **Practice**: Try implementing your own variations or additional features

## 📊 Data Structure Comparison

| Data Structure | Access | Search | Insert | Delete | Use Cases |
|----------------|--------|--------|--------|--------|-----------|
| Array | O(1) | O(n) | O(n) | O(n) | Lists, matrices |
| Linked List | O(n) | O(n) | O(1) | O(n) | Dynamic lists, undo/redo |
| Stack | O(n) | O(n) | O(1) | O(1) | Function calls, undo |
| Queue | O(n) | O(n) | O(1) | O(1) | Task scheduling, BFS |
| Binary Tree | O(log n) | O(log n) | O(log n) | O(log n) | Search, sorting |
| Hash Table | O(1) | O(1) | O(1) | O(1) | Dictionaries, caching |

## 🎓 Learning Path

1. **Start with Linked Lists** (current) - Understand basic node concepts
2. **Move to Stacks & Queues** - Learn about LIFO/FIFO principles
3. **Explore Trees** - Understand hierarchical relationships
4. **Study Hash Tables** - Learn about fast key-value access
5. **Master Graphs** - Understand complex relationships

## 🤝 Contributing

This is a learning repository! Feel free to:
- Add new data structure implementations
- Improve existing code with better algorithms
- Add unit tests and documentation
- Suggest new features or optimizations
- Create visualizations or diagrams

## 📝 Notes

- Each implementation focuses on clarity over optimization
- Code includes extensive comments for learning purposes
- Real-world applications are demonstrated through practical examples
- Performance analysis helps understand trade-offs

---

*This repository serves as a practical guide to understanding fundamental data structures through hands-on implementation and real-world applications.*


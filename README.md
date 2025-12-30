# fjzecopmlc-ds

A simple and efficient data structures library implemented in Python.

## Features

This library provides implementations of common data structures:

- **Stack**: Last-In-First-Out (LIFO) data structure
- **Queue**: First-In-First-Out (FIFO) data structure
- **LinkedList**: Singly linked list implementation

## Installation

You can install the package locally:

```bash
pip install -e .
```

## Usage

### Stack

```python
from fjzecopmlc_ds import Stack

# Create a new stack
stack = Stack()

# Push items
stack.push(1)
stack.push(2)
stack.push(3)

# Pop items (LIFO order)
print(stack.pop())  # 3
print(stack.pop())  # 2

# Peek at the top item
print(stack.peek())  # 1

# Check if empty
print(stack.is_empty())  # False

# Get size
print(stack.size())  # 1
```

### Queue

```python
from fjzecopmlc_ds import Queue

# Create a new queue
queue = Queue()

# Enqueue items
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue items (FIFO order)
print(queue.dequeue())  # 1
print(queue.dequeue())  # 2

# Check front item
print(queue.front())  # 3

# Check if empty
print(queue.is_empty())  # False

# Get size
print(queue.size())  # 1
```

### LinkedList

```python
from fjzecopmlc_ds import LinkedList

# Create a new linked list
ll = LinkedList()

# Append items
ll.append(1)
ll.append(2)
ll.append(3)

# Prepend items
ll.prepend(0)

# Find items
print(ll.find(2))  # True
print(ll.find(5))  # False

# Delete items
ll.delete(2)

# Check size
print(ll.size())  # 3

# Check if empty
print(ll.is_empty())  # False
```

## Testing

Run the tests using pytest:

```bash
pip install pytest
pytest tests/
```

## Development

To contribute to this project:

1. Clone the repository
2. Install development dependencies: `pip install -e .`
3. Make your changes
4. Run tests: `pytest tests/`
5. Submit a pull request

## License

MIT License

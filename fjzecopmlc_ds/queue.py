"""Queue implementation using collections.deque for efficient operations."""

from collections import deque
from typing import Any


class Queue:
    """A simple queue (FIFO) data structure implementation using deque."""

    def __init__(self):
        """Initialize an empty queue."""
        self._items: deque = deque()

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the rear of the queue.

        Args:
            item: The item to add to the queue.
        """
        self._items.append(item)

    def dequeue(self) -> Any:
        """
        Remove and return the front item from the queue.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def front(self) -> Any:
        """
        Return the front item without removing it.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0

    def size(self) -> int:
        """
        Return the number of items in the queue.

        Returns:
            The number of items in the queue.
        """
        return len(self._items)

    def __len__(self) -> int:
        """Return the number of items in the queue."""
        return self.size()

    def __str__(self) -> str:
        """Return a string representation of the queue."""
        return f"Queue({self._items})"

    def __repr__(self) -> str:
        """Return a detailed string representation of the queue."""
        return f"Queue({self._items!r})"

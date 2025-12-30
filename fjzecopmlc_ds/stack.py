"""Stack implementation using a list."""

from typing import Any


class Stack:
    """A simple stack (LIFO) data structure implementation."""

    def __init__(self):
        """Initialize an empty stack."""
        self._items: list[Any] = []

    def push(self, item: Any) -> None:
        """
        Add an item to the top of the stack.

        Args:
            item: The item to add to the stack.
        """
        self._items.append(item)

    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        """
        Return the top item without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0

    def size(self) -> int:
        """
        Return the number of items in the stack.

        Returns:
            The number of items in the stack.
        """
        return len(self._items)

    def __len__(self) -> int:
        """Return the number of items in the stack."""
        return self.size()

    def __str__(self) -> str:
        """Return a string representation of the stack."""
        return f"Stack({self._items})"

    def __repr__(self) -> str:
        """Return a detailed string representation of the stack."""
        return f"Stack({self._items!r})"

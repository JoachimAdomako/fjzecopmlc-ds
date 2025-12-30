"""Linked list implementation."""

from typing import Any, Optional


class Node:
    """A node in a linked list."""

    def __init__(self, data: Any):
        """
        Initialize a node with data.

        Args:
            data: The data to store in the node.
        """
        self.data = data
        self.next: Optional[Node] = None


class LinkedList:
    """A simple singly linked list implementation."""

    def __init__(self):
        """Initialize an empty linked list."""
        self._head: Optional[Node] = None
        self._size: int = 0

    def append(self, data: Any) -> None:
        """
        Add a node with data to the end of the list.

        Args:
            data: The data to add to the list.
        """
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, data: Any) -> None:
        """
        Add a node with data to the beginning of the list.

        Args:
            data: The data to add to the list.
        """
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def delete(self, data: Any) -> bool:
        """
        Delete the first node with the specified data.

        Args:
            data: The data to delete from the list.

        Returns:
            True if the data was found and deleted, False otherwise.
        """
        if self._head is None:
            return False

        if self._head.data == data:
            self._head = self._head.next
            self._size -= 1
            return True

        current = self._head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next

        return False

    def find(self, data: Any) -> bool:
        """
        Check if data exists in the list.

        Args:
            data: The data to search for.

        Returns:
            True if the data exists in the list, False otherwise.
        """
        current = self._head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def is_empty(self) -> bool:
        """
        Check if the list is empty.

        Returns:
            True if the list is empty, False otherwise.
        """
        return self._head is None

    def size(self) -> int:
        """
        Return the number of nodes in the list.

        Returns:
            The number of nodes in the list.
        """
        return self._size

    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        return self.size()

    def __str__(self) -> str:
        """Return a string representation of the list."""
        nodes = []
        current = self._head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        return f"LinkedList([{' -> '.join(nodes)}])"

    def __repr__(self) -> str:
        """Return a detailed string representation of the list."""
        return self.__str__()

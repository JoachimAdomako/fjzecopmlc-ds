"""Tests for the LinkedList data structure."""

import pytest
from fjzecopmlc_ds import LinkedList


def test_linked_list_initialization():
    """Test that a new linked list is empty."""
    ll = LinkedList()
    assert ll.is_empty()
    assert ll.size() == 0
    assert len(ll) == 0


def test_linked_list_append():
    """Test appending items to the linked list."""
    ll = LinkedList()
    ll.append(1)
    assert not ll.is_empty()
    assert ll.size() == 1
    ll.append(2)
    ll.append(3)
    assert ll.size() == 3


def test_linked_list_prepend():
    """Test prepending items to the linked list."""
    ll = LinkedList()
    ll.prepend(1)
    assert ll.size() == 1
    ll.prepend(2)
    ll.prepend(3)
    assert ll.size() == 3


def test_linked_list_find():
    """Test finding items in the linked list."""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.find(1)
    assert ll.find(2)
    assert ll.find(3)
    assert not ll.find(4)


def test_linked_list_delete():
    """Test deleting items from the linked list."""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.delete(2)
    assert ll.size() == 2
    assert not ll.find(2)
    assert ll.find(1)
    assert ll.find(3)


def test_linked_list_delete_head():
    """Test deleting the head of the linked list."""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.delete(1)
    assert ll.size() == 1
    assert not ll.find(1)
    assert ll.find(2)


def test_linked_list_delete_nonexistent():
    """Test deleting a non-existent item returns False."""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert not ll.delete(3)
    assert ll.size() == 2


def test_linked_list_delete_empty():
    """Test deleting from an empty list returns False."""
    ll = LinkedList()
    assert not ll.delete(1)


def test_linked_list_str_repr():
    """Test string representations of the linked list."""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert "LinkedList" in str(ll)
    assert "->" in str(ll)
    assert "LinkedList" in repr(ll)

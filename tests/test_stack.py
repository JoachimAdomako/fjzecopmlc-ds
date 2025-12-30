"""Tests for the Stack data structure."""

import pytest
from fjzecopmlc_ds import Stack


def test_stack_initialization():
    """Test that a new stack is empty."""
    stack = Stack()
    assert stack.is_empty()
    assert stack.size() == 0
    assert len(stack) == 0


def test_stack_push():
    """Test pushing items onto the stack."""
    stack = Stack()
    stack.push(1)
    assert not stack.is_empty()
    assert stack.size() == 1
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3


def test_stack_pop():
    """Test popping items from the stack."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.size() == 1
    assert stack.pop() == 1
    assert stack.is_empty()


def test_stack_pop_empty():
    """Test popping from an empty stack raises an error."""
    stack = Stack()
    with pytest.raises(IndexError, match="pop from empty stack"):
        stack.pop()


def test_stack_peek():
    """Test peeking at the top item."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert stack.size() == 2  # Size should not change
    assert stack.peek() == 2  # Should still be 2


def test_stack_peek_empty():
    """Test peeking at an empty stack raises an error."""
    stack = Stack()
    with pytest.raises(IndexError, match="peek from empty stack"):
        stack.peek()


def test_stack_str_repr():
    """Test string representations of the stack."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert "Stack" in str(stack)
    assert "Stack" in repr(stack)

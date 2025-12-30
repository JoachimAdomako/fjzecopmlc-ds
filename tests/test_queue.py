"""Tests for the Queue data structure."""

import pytest
from fjzecopmlc_ds import Queue


def test_queue_initialization():
    """Test that a new queue is empty."""
    queue = Queue()
    assert queue.is_empty()
    assert queue.size() == 0
    assert len(queue) == 0


def test_queue_enqueue():
    """Test enqueueing items into the queue."""
    queue = Queue()
    queue.enqueue(1)
    assert not queue.is_empty()
    assert queue.size() == 1
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.size() == 3


def test_queue_dequeue():
    """Test dequeuing items from the queue."""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.size() == 1
    assert queue.dequeue() == 3
    assert queue.is_empty()


def test_queue_dequeue_empty():
    """Test dequeuing from an empty queue raises an error."""
    queue = Queue()
    with pytest.raises(IndexError, match="dequeue from empty queue"):
        queue.dequeue()


def test_queue_front():
    """Test checking the front item."""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.front() == 1
    assert queue.size() == 2  # Size should not change
    assert queue.front() == 1  # Should still be 1


def test_queue_front_empty():
    """Test checking front of an empty queue raises an error."""
    queue = Queue()
    with pytest.raises(IndexError, match="front from empty queue"):
        queue.front()


def test_queue_str_repr():
    """Test string representations of the queue."""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert "Queue" in str(queue)
    assert "Queue" in repr(queue)

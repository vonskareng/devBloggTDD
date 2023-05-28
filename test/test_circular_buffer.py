import pytest
from src.circular_buffer import CircularBuffer

def test_is_empty_returns_true():
    buffer_size = 5
    circular_buffer = CircularBuffer(buffer_size)
    expected = True
    actual = circular_buffer.is_empty()
    assert actual == expected

def test_is_empty_returns_false_for_one_added_item():
    buffer_size = 5
    item = "first Item"
    circular_buffer = CircularBuffer(buffer_size)
    circular_buffer.enqueue(item)
    expected = False
    actual = circular_buffer.is_empty()
    assert actual == expected

def test_is_empty_returns_True_for_all_items_removed():
    buffer_size = 5
    item = "first Item"
    circular_buffer = CircularBuffer(buffer_size)
    circular_buffer.enqueue(item)
    circular_buffer.dequeue()
    expected = True
    actual = circular_buffer.is_empty()
    assert actual == expected

def test_is_full_returns_false_when_initialized():
    buffer_size = 5
    circular_buffer = CircularBuffer(buffer_size)
    expected = False
    actual = circular_buffer.is_full()
    assert actual == expected

def test_is_full_returns_true():
    buffer_size = 3 
    circular_buffer = CircularBuffer(buffer_size)
    item = "an awesome item"
    circular_buffer.enqueue(item)
    circular_buffer.enqueue(item)
    circular_buffer.enqueue(item)
    expected = True
    actual = circular_buffer.is_full()
    assert actual == expected

def test_is_full_returns_false_for_items_removed():
    buffer_size = 1
    circular_buffer = CircularBuffer(buffer_size)
    item = "an awesome item"
    circular_buffer.enqueue(item)
    circular_buffer.dequeue()
    expected = False
    actual = circular_buffer.is_full()
    assert actual == expected

def test_size_init():
    buffer_size = 2
    circular_buffer = CircularBuffer(buffer_size)
    actual_size = circular_buffer.size()
    expected = 0
    assert actual_size == expected

def test_size_with_one_item():
    buffer_size = 2 
    circular_buffer = CircularBuffer(buffer_size)
    item = "an awesome item"
    circular_buffer.enqueue(item)
    actual_size = circular_buffer.size()
    expected = 1
    assert actual_size == expected

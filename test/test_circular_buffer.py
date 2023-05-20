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
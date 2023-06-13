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
    for i in range(3):
        circular_buffer.enqueue("an awesome item")
    expected = True
    actual = circular_buffer.is_full()
    assert actual == expected

def test_is_full_returns_false_for_items_removed():
    buffer_size = 1
    circular_buffer = CircularBuffer(buffer_size)
    circular_buffer.enqueue("an awesome item")
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
    circular_buffer.enqueue("an awesome item")
    actual_size = circular_buffer.size()
    expected = 1
    assert actual_size == expected

def test_size_with_two_added_items_one_removed():
    buffer_size = 2 
    circular_buffer = CircularBuffer(buffer_size)
    for i in range(2):
        circular_buffer.enqueue("an awesome item")
    circular_buffer.dequeue()
    actual_size = circular_buffer.size()
    expected = 1
    assert actual_size == expected

def test_dequeue_returns_oldest_item():
    buffer_size = 3
    circular_buffer = CircularBuffer(buffer_size)
    item_one = "an awesome item"
    item_two = "an even more awesome item"
    circular_buffer.enqueue(item_one)
    circular_buffer.enqueue(item_two)
    oldest_item = circular_buffer.dequeue()
    expected = "an awesome item"
    assert oldest_item == expected

def test_dequeue_returns_none_if_empty():
    buffer_size = 3
    circular_buffer = CircularBuffer(buffer_size)
    actual = circular_buffer.dequeue()
    expected = None
    assert actual == expected

def test_dequeue_on_multiple_items():
    buffer_size = 3
    circular_buffer = CircularBuffer(buffer_size)
    for i in range(3):
        circular_buffer.enqueue(i)
    for i in range(3):
       assert circular_buffer.dequeue() == i

def test_enqueue_on_full_buffer():
    buffer_size = 2 
    circular_buffer = CircularBuffer(buffer_size)
    for i in range(3):
        circular_buffer.enqueue(i)
    actual = circular_buffer.dequeue()
    expected = 1
    assert actual == expected
    actual = circular_buffer.dequeue()
    expected = 2
    assert actual == expected
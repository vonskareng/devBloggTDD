import pytest

def test_is_empty():
    buffer_size = 5
    circularBuffer = CircularBuffer(buffer_size)
    expected = True
    actual = circularBuffer.is_empty()
    assert actual == expected
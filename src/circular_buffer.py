
class CircularBuffer():
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.circular_buffer = []

    def is_empty(self):
        return len(self.circular_buffer) == 0
    
    def is_full(self):
        return len(self.circular_buffer) == self.buffer_size
    
    def enqueue(self, item):
        self.circular_buffer.append(item)

    def dequeue(self):
        self.circular_buffer.pop()

    def size(self):
        return len(self.circular_buffer)
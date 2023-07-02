class CircularBuffer():
    def __init__(self, capacity):
        self.capacity = capacity
        self.circular_buffer = [None] * capacity
        self.reader = 0
        self.writer = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            self.circular_buffer[self.reader] = item
            self.reader = (self.reader + 1) % self.capacity
        else:
            self.circular_buffer[self.writer] = item
            self.writer = (self.writer + 1) % self.capacity
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.circular_buffer[self.reader]
        self.circular_buffer[self.reader] = None
        self.reader = (self.reader + 1) % self.capacity
        self.size -= 1
        return item

    def buffer_length(self):
        return self.size

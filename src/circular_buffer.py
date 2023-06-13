class CircularBuffer():
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.circular_buffer = []
        self.oldest = None

    def is_empty(self):
        return len(self.circular_buffer) == 0
    
    def is_full(self):
        return len(self.circular_buffer) == self.buffer_size

    def enqueue(self, item):
        if self.is_empty():
            self.oldest = 0
            self.circular_buffer.append(item)
        elif self.is_full():
            self.circular_buffer[self.oldest] = item
            self.oldest += 1
        else:
            self.circular_buffer.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        removed = self.circular_buffer.pop(self.oldest)
        if self.oldest > 0:
            self.oldest -= 1
        return removed
        
    def size(self):
        return len(self.circular_buffer)
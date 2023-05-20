
class CircularBuffer():
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.circular_buffer = []

    def is_empty(self):
        return len(self.circular_buffer) == 0
    
    
    def enqueue(self, item):
        self.circular_buffer = ["first Item"]



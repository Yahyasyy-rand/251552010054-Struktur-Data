from collections import deque

class martabak :
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.items_empty () :
            return self.items.popleft()
        return "martabak kosong"
    
    def peek (self):
        if not self.items_empty () :
            return self.items[0]
        
    def items_empty(self): return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def __str__(self): return str(list(self.items))
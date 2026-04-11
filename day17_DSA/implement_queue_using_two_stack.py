class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            return "Empty"
        
        return self.s2.pop()
    
q = QueueUsingStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())

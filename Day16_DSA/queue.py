class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return "queen is empty"
        return self.queue(0)
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Queue: ", q.queue)
print("Dequque: ",q.dequeue())
print("peek: ",q.peek())
print("size: ",q.size())
print("is empty: ",q.is_empty())
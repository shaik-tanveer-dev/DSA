class circularqueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return(self.rear + 1) % self.size == self.front
    
    def isEmpty(self):
        return self.front == -1
    
    def enqueue(self, data):
        if self.isFull():
            print("Queue is Full")
            return
        if self.isEmpty():
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print("Inserted: (data)")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        data = self.queue[self.front]

        if self.front == self.rear:
            self.front == self.rear == -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Deleted: {data}")

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.queue[self.front]
    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        
        print("Queue Element: ", end = " ")
        i = self.front
        while True:
            print(self.queue[i], end = " ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
cq = circularqueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
cq.enqueue(40)
cq.enqueue(50)
cq.display()
cq.enqueue(60) #circular in sertion
cq.display()

print("Front element :",cq.peek())
cq.dequeue()
cq.dequeue()
cq.display()

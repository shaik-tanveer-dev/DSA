from collections import deque

q = deque()

q.append(10)
q.append(20)
q.append(30)

print("Queue: ", q)

print("Dequeue: ", q.popleft())  
print("Peek: ", q[0])             
# Reversing a Queue (By using stack(list))

from collections import deque

q = deque([1, 2, 3, 4, 5])
stack = []

#step1: push into stack
while q:
    stack.append(q.popleft())

#step2: push back to Queue
while stack:
    q.append(stack.pop())

print("Reversed Queue: ", q)

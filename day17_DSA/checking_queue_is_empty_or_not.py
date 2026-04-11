#checking queue is empty or not

from collections import deque

q = deque([1, 2, 3, 4, 5])

if not q:
    print("Queue is empty")
else:
    print("Queue: ", q)


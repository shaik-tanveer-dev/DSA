from collections import deque

def reverse(dq, k):
    stack = []

    for _ in range(k):
        stack.append(dq.popleft())

    while(stack):
        dq.append(stack.pop())
    
    for _ in range(len(dq)-k):
        dq.append(dq.left())

    return dq

dq = deque([1,2,3,4,5])
k = 3
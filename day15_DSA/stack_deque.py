#By using deque

from collections import deque

stack = deque()

#push
stack.append(10)
stack.append(20)

print(stack)

#pop
stack.pop()
print(stack)

#peek
print(stack[-1])
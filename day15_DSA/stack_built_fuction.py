stack = []
#push
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print("Stack after pushing elements: ",stack)
#pop
removed = stack.pop()

print("poped element :",removed)
print("Stack after pop: ",stack)

#peek

top = stack[-1]
print("Top element: ", top)

#is empty
print("is empty stack",len(stack) == 0)
#size

print("Stack size:",len(stack))
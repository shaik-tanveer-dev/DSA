class stack:
    def __init__(self):
        self.stack = []
        #push
    def push(self, data):
        self.stack.append(data)
        #pop
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
        
        #peek
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
        
        #isempty
    def is_empty(self):
        return len(self.stack) == 0
       #size
    def size(self):
        return len(self.stack)
    

s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(50)


print(f"Top : {s.peek()} ")
print(f"Popped: {s.pop()}" )
print(f"size : {s.size()}")
print(f"is empty: {s.is_empty()}")
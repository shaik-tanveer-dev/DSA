#checking valid parenthieses

def isvalid(s):
    stack = []
    mapping = {'(':')','[':']','{':'}'}

    for ch in s:
        if ch in mapping:
            if not stack or stack[-1] != mapping:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0

s = input("Enter a string of brackets: ") 

if isvalid(s):
    print("Valid paranthese")
else:
    print("Invalid paranthese")
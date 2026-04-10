def isBalance(s):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

s = input("Enter a string of barckets:")

if isBalance(s):
    print("valid parenthersis")
else:
    print("Invalid paraentehsis")
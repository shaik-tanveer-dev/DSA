#Deque implementation usage of package dequeu
#Deque is double ended queue
#insertion and deletion at both the ends
# -->Insert from front -->appendleft()
# -->Insert from Rear -->append()
# -->delete from front -->popleft()
# -->Delete from rear -->pop()

from collections import deque
dq = deque()
#inserting elements
dq.append(18)
dq.append(20)
dq.append(5)
print("Deque after Insertion: ", dq)
#delete elements
dq.pop()
print("After Insertion: ",dq)
dq.popleft()
print("After popleft: ",dq)
#add more elements
dq.append(30)
dq.append(40)
print("Final deque: ",dq)
#peek
print("Final Element: ", dq[0])
print("Rear Element: ",dq[-1])

#size
print("Size: ",len(dq))
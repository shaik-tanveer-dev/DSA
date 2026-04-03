# Linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_position(self,pos,data):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                return
            temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def delete_from_beginning(self):
        if self.head:
            self.head = self.head.next
    def delete_from_ending(self):
        #having empty list
        if self.head is None:
            return
        #having single element in list
        if self.head.next is None:
            self.head = None
            return
        #having elements in linked list
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_value(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
            temp = temp.next
        
    def delete_at_position(self, pos):
        if self.head is None:
            return
        if pos == 0:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(pos -1):
            if temp.next is None:
                return
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def search(self,key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    #Access by position
    def get(self, pos):
        temp = self.head
        for _ in range(pos):
            if temp is None:
                return None
            temp = temp.next
        return temp.data if temp else None
    
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next #store next node
            curr_next = prev #reverse linked list
            prev = curr #move prev
            curr = next_node # move curr
        
        self.head = prev
    #function to detect cycle(Floyed's Algorithm)
    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

# l1 = LinkedList()
# l1.insert_at_beginning(10)
# l1.insert_at_beginning(5)
# l1.insert_at_end(20)
# l1.insert_at_end(30)
# l1.display() #5->15->10->20->30->Null
# l1.insert_at_position(2,15)
# l1.display()
# print(l1.search(20))
# l1.delete_value(20)
# l1.delete_from_beginning()
# l1.display()
# l1.delete_from_ending()
# l1.display()

# l1.reverse()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

#Linking nodes
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

#Create Cycle
n5.next = n3
#Assign head
ll = LinkedList()
ll.head = n1
#check cycles
print(ll.has_cycle())

class node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class doublylinkedlist:
    def __init__(self):
        self.head=None

    def insert_begin(self,data):
        new_node=node(data)

        if self.head:
            self.head.prev=new_node
            new_node.next=self.head

        self.head=new_node

    def insert_end(self,data):
        new_node=node(data)

        if self.head is None:
            self.head=new_node
            return
        
        temp=self.head
        while temp.next:
            temp =temp.next
        temp.next=new_node
        new_node.prev=temp

    def insert_at_pos(self,pos,data):
        new_node=node(data)

        if pos==0:
            self.insert_begin(data)
            return
        
        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                return
            temp=temp.next

        if temp.next:
            temp.next.prev=new_node
        
        new_node.next=temp.next
        new_node.prev=temp
        temp.next=new_node

    def delete_begin(self):
        if self.head is None:
            return
        
        self.head = self.head.next

        if self.head:
            self.head.prev = None
    
    def delete_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def delete_value(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next

    def delete_at_position(self,pos):
        if self.head is None:
            return
        
        if pos==0:
            self.delete_begin()
            return
        
        temp=self.head
        for _ in range(pos):
            if temp is None:
                return
            temp=temp.next

        if temp.prev:
            temp.prev.next=temp.next
        if temp.next:
            temp.next.prev=temp.prev

    def get(self,pos):
        temp=self.head
        for _ in range(pos):
            if temp is None:
                return None
            temp=temp.next 
        return temp.data if temp else None
    
    def search(self,key):
        temp=self.head
        while temp:
            if temp.data==key:
                return True
            temp=temp.next
        return False
    
    def update(self,pos,value):
        temp=self.head
        for _ in range(pos):
            if temp is None:
                return
            temp=temp.next

        if temp:
            temp.data=value
    
    def update_value(self,old,new):
        temp=self.head
        while temp:
            if temp.data == old:
                temp.data = new
                return
            temp = temp.next

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")


# Testing
dll = doublylinkedlist()

dll.insert_begin(10)
dll.insert_begin(5)
dll.insert_begin(20)
dll.insert_begin(30)

dll.display()

dll.insert_at_pos(2,15)
dll.display()

print(dll.get(2))
print(dll.search(20))

dll.delete_value(15)
dll.display()

dll.update(1,99)
dll.display()

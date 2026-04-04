class node:
    def _init_(self,data):
        self.prev = None
        self.data = data
        self.next = None

class doublylinkedlist:
    def _init_(self):
        self.head=None

    #inserting operations
    #inserting at beginning
    def insert_begin(self,data): # o(1)
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
            new_node.prev=temp.next

        temp.next=new_node
        new_node.prev=temp

    #Deletion

    def delete_begin(self):
        if self.head is None:
            return
        
        self.head = self.head.next

        if self.head:
            self.head.prev = None
    
    def delete_end(self):  #o(n)
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
        if self.head is None:
            return
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

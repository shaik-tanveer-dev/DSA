class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):         
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head   
        self.head = new_node

    def insert_at_end(self, data):
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
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")



l1 = LinkedList()
l1.insert_at_beginning(10)
l1.insert_at_beginning(5)
l1.insert_at_end(20)
l1.insert_at_end(30)

l1.display()   
print(l1.search(20))

l1.delete_from_beginning()
l1.display()

l1.delete_from_ending()
l1.display()
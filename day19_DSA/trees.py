class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# traversal functions

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def main():
    # create nodes
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    # connecting nodes
    root.left = node2
    root.right = node3

    node2.left = node4
    node2.right = node5

    print("\nInorder Traversal:")
    inorder(root)

    print("\nPreorder Traversal:")
    preorder(root)

    print("\nPostorder Traversal:")
    postorder(root)

main()
from collections import deque

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Count total nodes
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Count leaf nodes
def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


# Height of tree (number of levels)
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


# Level order traversal (returns list instead of printing)
def level_order(root):
    if root is None:
        return []

    result = []
    q = deque([root])

    while q:
        node = q.popleft()
        result.append(node.data)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return result


# Optimized single traversal (advanced)
def analyze_tree(root):
    if root is None:
        return 0, 0, 0  # nodes, leaves, height

    left_nodes, left_leaves, left_height = analyze_tree(root.left)
    right_nodes, right_leaves, right_height = analyze_tree(root.right)

    total_nodes = 1 + left_nodes + right_nodes

    if root.left is None and root.right is None:
        total_leaves = 1
    else:
        total_leaves = left_leaves + right_leaves

    total_height = 1 + max(left_height, right_height)

    return total_nodes, total_leaves, total_height


# Main function
def main():
    # Creating tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Basic functions
    print("Total nodes:", count_nodes(root))
    print("Height:", height(root))
    print("Leaf Nodes:", count_leaves(root))

    print("Level Order Traversal:", level_order(root))

    # Optimized analysis
    nodes, leaves, h = analyze_tree(root)
    print("\nUsing Single Traversal:")
    print("Total nodes:", nodes)
    print("Leaf nodes:", leaves)
    print("Height:", h)


# Driver code
if __name__ == "__main__":
    main()

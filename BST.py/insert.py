# Python program to demonstrate insert operation in binary search tree

# A utility class that represents an individual node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert a new node with the given key
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)


def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)


r = Node()
insert(r, Node(334))
insert(r, Node(2))
insert(r, Node(440))
insert(r, Node(700))
insert(r, Node(603))
insert(r, Node(8))


print("inorder: ")
inorder(r)
print("post order: ")
post_order(r)
print("pre order: ")
pre_order(r)
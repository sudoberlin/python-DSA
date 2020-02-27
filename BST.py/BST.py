class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BinarySearchTree():
    def __init__(self, root = None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_helper(self.root, key)


    def insert_helper(self, node, key):
        if node.key > key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert_helper(node.left, key)

        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert_helper(node.right, key)


    def find_inorder_succesor(self,node):
        myval = node
        while myval.left is not None:
            myval = myval.left
        return  myval

    def delete_node(self,node,key):
        if node is None:
            return node
        if key < node.key:
            node.left = self.delete_node(node.left,key)
        elif key > node.key:
            node.right = self.delete_node(node.right,key)
        else:
            # case with no child or 1 child
            if node.left is None:
                temp = node.right
                node = None

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # case with 2 children
            temp = self.find_inorder_succesor(node.right)

            node.key = temp.key
            node.right = self.delete_node(node, temp.key)
        return node


    def search(self,node,key):
        if node is None:
            print("key not found")
            return False
        elif node == key:
            print ("found key")
            return True
        elif key < node.key:
            self.search(node.left, key)
        else:
            self.search(node.right, key)


    # Inorder preorder postorder traversal
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.key, ", ", end='')
            self.inorder(node.right)

    def preorder(self,node):
        if node:
            print(node.key, ', ', end='')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, ', ', end='')

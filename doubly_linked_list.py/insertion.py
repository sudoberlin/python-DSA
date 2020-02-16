import gc  # garbage Collector


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doublyllist:
    def __init__(self):
        self.head = None


    def push(self, new_value):
        new_node = Node(new_value)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node


    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("prev_node can not be None")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node


    def addatend(self, new_value):
        new_node = Node(new_value)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        end_node = self.head
        while(end_node.next is not None):
            end_node = end_node.next

        end_node.next = new_node
        new_node.prev = end_node
        return

    def deletenode(self, key):
        if self.head is None or key is None:
            return

        #case-1
        if self.head == key:
            self.head = key.next

        #case-2
        if key.next is not None:
            key.next.prev = key.prev

        #case-3
        if key.prev is not None:
            key.prev.next = key.next

        gc.collect()



    def printdllist(self, node):
        while(node is not None):
            print(node.data, end=" ")
            node = node.next

if __name__ == "__main__":

    dll = Doublyllist()
    
    dll.push(1)
    dll.push(2)
    dll.push(3)

    dll.printdllist(dll.head)


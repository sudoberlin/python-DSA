# push, append and Insertion method of Linked List
# Node class
class Node:

    #function to initialize the node object

    def __init__(self,data):
        self.data = data    # assign data
        self.next = None    # initialize next as none
# linkedlist class contains a node object
class LinkedList:

    # function to initialize head
    def __init__(self):
        self.head = None

    # function to add a new node object at the beginning
    def push (self,new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    # inserts new node after the given prev_node
    def InsertAt(self, prev_node, new_value):
        if prev_node is Node:
            print("previous node seems to be empty")
            return
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # appends a new node object at the end
    def append(self, new_value):
        new_value = Node(new_value)

        if self.head is None :
            self.head = new_value
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_value
    # function to print the linkedlist
    def printlist (self):
        tmp = self.head
        while (tmp):
            print (tmp.data)
            tmp = tmp.next
    
    # function to reverse a linked list
    def reversellist(self):
        prev = None
        curr = self.head  #initialize head as current value

        while curr is not None :
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


#code execution
if __name__ == "__main__":

    llist = LinkedList()
    llist.append(10)
    llist.push(1)
    llist.append(9)
    llist.push(2)
    llist.push(3)
    llist.InsertAt(llist.head.next,8)
    llist.push(4)
    llist.push(5)
    llist.append(7)
    llist.InsertAt(llist.head.next,6)

    print("created linked list is: ")
    llist.printlist()

    print("reversed linked list is : ")
    llist.reversellist()
    llist.printlist()

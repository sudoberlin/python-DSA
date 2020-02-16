class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Circularllist:
    def __init__(self):
        self.head = None

    def push (self, data):
        new_node = Node(data)
        temp = self.head

        new_node.next = self.head

        if self.head != None:
            while(temp.next != self.head):
                temp = temp.next

            temp.next = new_node

        else:
            new_node.next = new_node
            
        self.head = new_node

    def printcllist(self):
        temp = self.head
        if self.head != None:
            while(True):
                print(temp.data)
                temp = temp.next
                if (temp == self.head):
                    break


cllist = Circularllist()
cllist.push(1)
cllist.push(2)
cllist.push(3)
cllist.push(9)
cllist.printcllist()


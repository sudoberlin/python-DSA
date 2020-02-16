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

    def delete(self, key):
        current_node = self.head
        prev_node = None

        while(current_node):
            if current_node.data == key and current_node == self.head:
                # case -1
                #head is the only element in cllist
                if current_node.next == self.head:
                    current_node = None
                    self.head = None
                    return

                #case -2
                # if there are more element in the clist
                else:
                    # traverse and update head, delete head
                    while current_node.next != self.head:
                        current_node = current_node.next
                        current_node.next = self.head.next
                        self.head = self.head.next
                        current_node =None
                        return

            elif current_node.data == key:
                prev_node.next = current_node.next
                current_node = None
                return

            else:
                if current_node.next == self.head:
                    break


            prev_node = current_node
            current_node = current_node.next




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

cllist.delete(9)
cllist.printcllist()

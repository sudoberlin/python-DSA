#  34, 45, 67, 78, 89, 12, 23, 31
#   0,  1,  2,  3,  4,  5,  6,  7
#        R  F

# (self.rear + 1) % self.size == self.front
# 2%8 == 2

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range (size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if ((self.rear +1) % self.size == self.front):
            print("queue is full")
            return
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if (self.front == -1):
            print("queue is already empty")
            return
        elif(self.front ==self.rear):
            popval = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return popval
        else:
            popval = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return popval


cq = CircularQueue(5)
cq.enqueue(14)
cq.enqueue(22)
cq.enqueue(13)
cq.enqueue(-6)
print("Deleted value = ", cq.dequeue())
print("Deleted value = ", cq.dequeue())
print("Deleted value = ", cq.dequeue())
cq.enqueue(9)
cq.enqueue(20)
cq.enqueue(5)
print(cq)
print("Deleted value = ", cq.dequeue())
print("Deleted value = ", cq.dequeue())
print("Deleted value = ", cq.dequeue())
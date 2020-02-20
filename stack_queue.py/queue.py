# Enqueue-adds an intem to the queue, if queue is full-overflow condition
# dequeue-renoves an item from the queue in FIFO order, if the queue is empty-underflow condition
# Front- get the front item from the queue
# Rear- get the last item from the queue

# implementation using list

queue = []
# using 'append()' function to push
queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")

print('queue: ', queue)

# pop() function to pop/delete element from queue in FIFO order
print("\nelements popped from the queue: ")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nqueue after elements are popped out: ", queue)
# print(queue.pop(0)) # this will raise a index error as pop from empty list


## implementations using collections.deque
from collections import deque

# initializing a queue
queue = deque()
# using 'append()' function to push
queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")

print('queue: ', queue)

# removing elements from queue using popleft()
print("\nelements popped from the queue: ")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print("\nqueue after elements are popped out: ", queue)
# print(queue.popleft()) # this will raise a index error as queue is emty now


### implementation using queue module
from queue import Queue

# initializing a queue
queue = Queue(maxsize=3)  # maxsize- number of items allowed in the queue
print(queue.qsize())  # qsize()- give maxsize of the stack

# put()- function to push
queue.put("a")
queue.put("b")
queue.put("c")

print("full: ", queue.full())  # full() – Return True if there are maxsize items in the queue.
# If the queue was initialized with maxsize=0 (the default), then full() never returns True.
print("size: ", queue.qsize())
# using get() function to pop out the element
print("\nelements popped from the stack: ")
print(queue.get())
print(queue.get())
print(queue.get())

print("\nempty: ", queue.empty())  # empty() – Return True if the queue is empty (False otherwise).

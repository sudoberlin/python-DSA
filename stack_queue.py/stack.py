# python program to demonstrate stack implementation using list
stack = []
#using 'append()' function to push
stack.append("black")
stack.append("blue")
stack.append("white")
stack.append("red")

print('stack: ',stack)

#pop() function to pop/delete element from stack in LIFO order
print("\nelements popped from the stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("\n stack after elements are popped out: ",stack)

## implementation using collection.deque

from collections import deque
stack = deque()
# append() function to push
stack.append("black")
stack.append("blue")
stack.append("white")

print('stack: ',stack)

#pop() function to pop element in LIFO order
print("\nelements popped from the stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\n stack after elements are popped out: ",stack)


### implementation using queue module

from queue import LifoQueue

#initializing a stack
stack = LifoQueue(maxsize = 3) # maxsize- number of items allowed in the queue
print(stack.qsize()) # qsize()- give maxsize of the stack

#put()- function to push
stack.put("black")
stack.put("blue")
stack.put("white")

print("full: ",stack.full()) #full() – Return True if there are maxsize items in the queue.
# If the queue was initialized with maxsize=0 (the default), then full() never returns True.
print("size: ",stack.qsize())
# using get() function to pop out the element
print("\nelements popped from the stack: ")
print(stack.get())
print(stack.get())
print(stack.get())

print("\nempty: ",stack.empty()) # empty() – Return True if the queue is empty (False otherwise).
import sys
sys.setrecursionlimit(1000000)

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


num = int(input("enter a number: "))


if num < 0:
    print ("enter postive number")
elif num == 0:
    print("factorial is : 1")
else:
    print("factorial is: ",factorial(num))



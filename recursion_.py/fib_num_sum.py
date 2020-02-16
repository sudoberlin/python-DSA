def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1)+fib(n-2))


count = int(input("enter a number: "))
if count <= 0:
    print ("enter a higher value")
else:
    sum = 0
    for i in range (count):
        sum = sum + fib(i)
    print (sum)

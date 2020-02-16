def fib(n):
    if n<=1: 
        return n
    else:
        return (fib(n-1)+fib(n-2))

count = int(input ("enter a number"))
if count <= 0 :
    print ("enter value greater than 2")
else:
    for i in range (count):
        last_value = fib(i)

    print(last_value)

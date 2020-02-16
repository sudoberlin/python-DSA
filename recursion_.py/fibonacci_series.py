def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))


count = int(input("enter a number: "))
if count <= 0:
    print("plese! enter value greater than 2")
else:
    for i in range (count):
        print (fibonacci (i),end = " \n")

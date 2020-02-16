def factorial(n):
    res = 1
    for i in range (2,n+1):
        res = res * i
    return res


def combination(n, r):
    return factorial(n) /(factorial(r) * factorial(n-r)) 

n = int(input ("enter a number: "))
r = int(input("enter a number: "))
print (int(combination(n,r)))

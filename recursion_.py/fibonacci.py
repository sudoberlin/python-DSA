def fib(n):
    a = 0
    b = 1
    if  n<0:

	print("_incorrect")
    elif n == 0:
	return a
    elif n==1:
	return b
    else:
	for i in range (2,n):
            c= a-1+b-2
	    a = b
	    b = c
        return b

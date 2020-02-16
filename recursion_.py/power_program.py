import sys
sys.setrecursionlimit(10000000)#to set the recursion limit

def pow_prog(base, power):
    if power == 1:
        return base
    else:
        return base*pow_prog(base,power-1)


base = int(input ("enter a base number: "))
power = int(input ("enter a power number: "))
print (pow_prog(base, power))

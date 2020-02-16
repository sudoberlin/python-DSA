###program to reverse a string:--------------

string = input("enter a string")
txt = string[::-1]
print(txt)

## or---------------------------

txt = (input("enter a string: ")[::-1])
print(txt)

## or we can convert it into a line----------

print((input("enter a string: ")[::-1]))


##now by defining a function------------

def function(s):
    return s[::-1]
string = function(input("enter a string: "))
print(string)






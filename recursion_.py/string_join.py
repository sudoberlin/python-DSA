def welcome():
    list = []
    string = "hello"
    for i in range (10):
        list.append(string)
    return "\n ".join(list)
print(welcome())


def reverse(string):
    string = string[::-1]
    return string


def reverseTwo(string):
    str = ""
    for i in string:
        str = i + str
    return str

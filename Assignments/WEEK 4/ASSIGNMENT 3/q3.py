"""
Write a Python program to check whether an element exists within a tuple. Ask something from user, if that exists in tuple, then print “YES” else print “NO”.

"""


def elementExistsInTuple(element, t):
    return element in t


my_tuple = (8, 46, 23, 42, 21, 17, 50, 13, 10, 6, 46, 41)

e = int(input("Enter an element = "))

if elementExistsInTuple(e, my_tuple):
    print("YES")
else:
    print("NO")

"""
Write a Python program to check whether an element exists within a tuple. Ask something from user, if that exists in tuple, then print “YES” else print “NO”.

"""


def check_item_exists(t, n):
    if t.count(n) > 0:
        return "YES"
    else:
        return "NO"


my_tuple = (8, 46, 23, 42, 21, 17, 50, 13, 10, 6, 46, 41)
number = int(input("Enter a number to find within given tuple: "))
result = check_item_exists(my_tuple, number)
print(result)

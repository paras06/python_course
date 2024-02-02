"""
Write a Python program to reverse a tuple.

"""


def reverse_tuple(t):
    result = []
    for item in range(len(t) - 1, 0, -1):
        result.append(t[item])

    return tuple(result)


my_tuple = (8, 46, 23, 42, 21, 17, 50, 13, 10, 6, 46, 41)
result = reverse_tuple(my_tuple)
print(result)

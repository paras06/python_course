"""
Write a Python program to find repeated items in a tuple.

"""


def find_repeated_item(t):
    list1 = []
    result = []
    for item in t:
        if t.count(item) > 1:
            list1.append(item)

    for i in list1:
        if i not in result:
            result.append(i)

    return result


# def remove_duplicate_from_list(l):
#     result = []
#     for item in l:
#         if item not in result:
#             result.append(item)

#     return result


my_tuple = (1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 8, 9)
print(f"Repeated items in the tuple are: {find_repeated_item(my_tuple)}")

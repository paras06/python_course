"""
Write a function to remove duplicates from a list and print them.

"""


def removeDuplicate(lst):
    # initializing list

    print("The original list is : " + str(lst))

    res = []
    for i in lst:
        if i not in res:
            res.append(i)

    # printing list after removal
    print("The list after removing duplicates : " + str(res))


test_list = [1, 5, 3, 6, 3, 5, 6, 1]

lst = removeDuplicate(test_list)
print(lst)

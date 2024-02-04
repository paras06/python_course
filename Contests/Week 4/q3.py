"""
Python Program to remove all duplicates from a given string.

"""


def removeDuplicates(str):
    result = ""
    for i in str:
        if i not in result:
            result += i

    return result


print(removeDuplicates("hheeelllooo"))

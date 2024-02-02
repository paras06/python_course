"""
Write a Python code to find the second largest element in a list without sorting.

"""


def remove_duplicate(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result


def find_second_largest(lst):
    temp = []
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i + 1] = lst[i]
            temp.append(lst[i + 1])
        else:
            lst[i] = lst[i + 1]
            temp.append(lst[i])

    result = remove_duplicate(temp)
    print(f"The second largest element in the given list is: {result[-2]}")


my_list = [54, 1, 4, 56, 67, 879, 22]
output = find_second_largest(my_list)

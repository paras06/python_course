"""
Write a python program to check if the list contains three consecutive common numbers in Python.

"""


def sort(lst):
    temp = 0
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            temp = lst[i + 1]
            lst[i + 1] = lst[i]
            lst[i] = temp

            sort(lst)
    return lst


def get_consecutive_number_count(lst):
    flag = False
    for i in range(0, len(lst) - 2):
        if lst[i] == lst[i + 1] == lst[i + 2]:
            flag = True
            print(lst[i], end=" ")

    if flag == False:
        print("No")


# my_list_1 = [4, 5, 5, 5, 3, 8]
# my_list_1 = [1, 1, 1, 64, 23, 64, 22, 22, 22]
my_list_1 = [54, 1, 4, 56, 67, 879, 22]
get_consecutive_number_count(my_list_1)

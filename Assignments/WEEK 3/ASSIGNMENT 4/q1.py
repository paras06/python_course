"""
Make a list of your own. Make two more empty list like odd and even.
Put all the even numbers from original list to even and odd numbers to add
and print both lists. (Don’t remove anything from original one).

"""


def listEvenOdd(lst):
    lst_even, lst_odd = [], []
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            lst_even.append(lst[i])
        else:
            lst_odd.append(lst[i])

    return lst_even, lst_odd


my_list = [34, 11, 91, 59, 33, 22]
result = listEvenOdd(my_list)
print("Even list is: {result[0]}")
print("Odd list is: {result[1]}")

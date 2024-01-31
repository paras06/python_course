"""
Create a function sumCountOddEven
that accepts an List of Integers and calculate sum of even and odd numbers.


lst = [34, 11, 91, 59, 33, 22]

Output
Even numbers sum = 56
Odd numbers sum = 194

"""


def sumCountOddEven(my_list):
    sum_odd, sum_even = 0, 0
    for i in my_list:
        if i % 2 == 0:
            sum_even = sum_even + i
        else:
            sum_odd = sum_odd + i

    print(f"Even numbers sum = {sum_even}")
    print(f"Odd numbers sum = {sum_odd}")


lst = [34, 11, 91, 59, 33, 22]
sumCountOddEven(lst)

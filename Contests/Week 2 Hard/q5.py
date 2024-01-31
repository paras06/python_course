"""
Make a function named sumOfFirstAndLastDigit which accepts an integer n
from the user. Calculate the sum of first and last digit of a number and return it.
"""


def reverse(num: int) -> int:
    n = num
    result = 0
    while n > 0:
        last_digit = n % 10
        result = (result * 10) + last_digit
        n = n // 10
    return result


def sumOfFirstAndLastDigit(n):
    num = n
    first_digit = 0
    last_digit = 0

    if num <= 9:
        return num
    else:
        last_digit = n % 10
        first_digit = reverse(n) % 10

    return first_digit + last_digit


# def sumOfFirstAndLastDigit(num: int) -> int:
#     if num <= 9:
#         return num
#     n = num
#     last_digit = n % 10
#     while n > 0:
#         if n <= 9:
#             first_digit = n
#             break
#         n = n // 10
#     return first_digit + last_digit


print(sumOfFirstAndLastDigit(11))

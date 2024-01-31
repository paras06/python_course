"""
Create a function addDigits()
that takes an integer as an argument. Calculate the sum of digits of that number.
"""


def addDigits(num):
    n: int = num
    total = 0
    while n > 0:
        total = total + (n % 10)  # n%10 gives us last digit
        n = n // 10
    return total


# def addDigits_1(num):
#     n: int = num
#     total = 0
#     for n in range
#         total = total + (n % 10)  # n%10 gives us last digit
#         n = n // 10
#     return total

print(addDigits(454545))

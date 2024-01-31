"""
Make a function named sumPattern that takes an integer n
as an argument from the user. And then calculate the sum of the following pattern.

"""


def factorial(num: int) -> int:
    i: int = 1
    fact: int = 1
    while i <= num:
        fact = fact * i
        i = i + 1
    return fact


def sumPattern(n: int) -> float:
    i: int = 1
    total: float = 0

    while i <= n:
        total = total + (1 / factorial(i))

        i = i + 1

    return total


print(sumPattern(5))

"""
Write a Python program to generate a list of prime numbers less than
500 using list comprehension.
Example output: [2, 3, 5, 7, 11, 13, 17, 19, 23, ..., 491, 499]
500 can be changed to anything.

"""


def isPrime(num: int) -> bool:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


my_list = [i for i in range(1, 5000) if isPrime(i) == True and i < 500]
print(my_list)

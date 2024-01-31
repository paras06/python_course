"""
Generate a list of numbers less than 1000 which are divisible by the sum of their digits. (These were solved in contests)
Output: 
"""


def checkDivisible(n):
    num = n
    total = 0
    while n > 0:
        last_digit = n % 10
        total = total + last_digit
        n = n // 10

    if num % total == 0:
        return True
    else:
        return False


lst = [i for i in range(1, 1000) if checkDivisible(i)]
print(lst)

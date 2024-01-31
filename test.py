import math


def sumofalldivisorsopt(num):
    sum1 = 0
    sqrt = int(math.sqrt(num))
    for i in range(1, sqrt + 1):
        if num % i == 0 and i != sqrt:
            sum1 += i
            sum1 += int(num / i)
        elif i == sqrt:
            sum1 += i
    return sum1

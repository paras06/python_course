# import math


# def sumofalldivisorsopt(num):
#     sum1 = 0
#     sqrt = int(math.sqrt(num))
#     for i in range(1, sqrt + 1):
#         if num % i == 0 and i != sqrt:
#             sum1 += i
#             sum1 += int(num / i)
#         elif i == sqrt:
#             sum1 += i
#     return sum1


def add(n1, n2, n3, n4):
    sum = n1 + n2 + n3 + n4
    print(sum)

    # return sum


# print(add(2, 3, 4, 5))


add(2, 3, 4, 5)

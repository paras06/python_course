"""
Q1. Create a function named div_by_3_and_5 which takes 2 integers as a arguments (n1,n2), and print all the numbers divisible by 3 and 5 between n1 and n2.

"""


def div_by_3_and_5(n1: int, n2: int):
    start = n1
    end = n2
    while start <= end:
        if start % 3 == 0 and start % 5 == 0:
            print(start, end=" ")

        start += 1


x = div_by_3_and_5(10, 30)
print(x)

"""
Create a function named calSum() which takes 2 integers n1 and n2 as
a argument. Calculate the sum of all the numbers from n1 and n2 and
RETURN THAT SUM. Also make sure that n1 is smaller than n2. If it is not,
then return “n1 should be smaller”.

"""


def calSum(n1: int, n2: int):
    start = n1 if n1 < n2 else n2
    end = n2 if n1 < n2 else n1
    sum = 0

    if n1 > n2:
        print("n1 should be smaller")
        return

    while start <= end:
        sum += start
        start += 1
    return sum


x = calSum(10, 0)
print(x)

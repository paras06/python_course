"""
Create a function named calSum which takes an 2 integer (n1 and n2)
as an argument. Calculate the sum of all the numbers divisible by 5
between n1 and n2 and return that sum. (Make sure that n1 is less than n2)

"""


def calSum(n1, n2):
    start = n1 if n1 < n2 else n2
    end = n2 if n1 < n2 else n1
    sum = 0
    if n1 > n2:
        print("n1 should be smaller")
        return

    while start <= end:
        if start % 5 == 0:
            sum += start
        start += 1

    return sum


x = calSum(43, 68)
print(x)

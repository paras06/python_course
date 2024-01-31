"""
Q5. Create a function named printPattern that takes one integer (num) as
an argument. Print from -num to num. Also keep in mind number passed as
an argument can be negative or positive.

"""


def printPattern(num):
    i = 0
    x = num
    if num > 0:
        x = -1 * num
    else:
        num = -1 * num

    while x <= num:
        print(x, end=" ")
        x = x + 1


printPattern(-10)

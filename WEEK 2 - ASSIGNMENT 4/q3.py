"""
Q3.
Create a function named pattern which takes an integer as an input and print the following pattern.

"""


def pattern(n):
    i = 0

    while i < n:
        print(2**i, end=" ")
        i += 1


pattern(7)

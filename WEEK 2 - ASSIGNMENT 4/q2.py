"""
Q2.
Create a function named pattern which takes an integer as an input and print the following pattern.
"""


def pattern(n):
    i = 1
    while i <= n:
        print(i * 10, end=" ")
        i += 1


pattern(4)

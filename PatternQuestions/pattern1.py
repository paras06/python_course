"""
    * 
   * *
  * * *
 * * * *
* * * * *

"""


def pattern1(n):
    n = 5
    i = 0
    while i <= n:
        print(" " * (n - i) + "x" * i)
        i += 1

    # number of spaces
    k = n - 1

    # outer loop to handle number of rows
    for i in range(0, n):
        # inner loop to handle number spaces
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("x ", end="")

        # ending line after each row
        print("\r")


# def pattern(n):
#     for i in range(1, n):
#         for j in range(1, n - i):
#             print(" ", end=" ")
#         for k in range(1, i + 1):
#             print(i, end=" ")
#         print()


# pattern(6)


def pattern(n):
    for i in range(n, 0, -1):
        for j in range(n - i, 1, -1):
            print(" ", end=" ")
        print()
        for k in range(n, i - 1, -1):
            print(k, end=" ")


pattern(5)

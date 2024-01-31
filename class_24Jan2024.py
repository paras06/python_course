"""
        x 
      x x
    x x x
  x x x x
x x x x x


def pattern(n):
    k = n - 1
    for i in range(1, n + 1):
        for k in range(1, n + 1 - i):
            print(" ", end=" ")
            k = k - i

        for j in range(1, i + 1):
            print("x", end=" ")

        print()


pattern(5)

"""

"""
    x 
   x x
  x x x
 x x x x
x x x x x

def pattern(n):
    k = n - 1
    for i in range(1, n + 1):
        for k in range(1, n + 1 - i):
            print("", end=" ")
            k = k - i

        for j in range(1, i + 1):
            print("x", end=" ")

        print()


pattern(5)

"""
"""
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5 

"""


def pattern_1(n):
    k = n - 1
    for i in range(1, n + 1):
        for k in range(1, (n + 1) - i):
            print(" ", end=" ")
            k = k - i

        for j in range(1, i + 1):
            print(i, end=" ")

        print()


"""
        5 
      4 5
    3 4 5
  2 3 4 5
1 2 3 4 5

"""


def pattern_3(n):
    k = n - 1
    for i in range(n, 0, -1):
        for k in range(1, (i + 1) - 1):
            print(" ", end=" ")
        for j in range(i, n + 1):
            print(j, end=" ")
        print()


pattern_3(5)

# *********************************************************************


def pattern_2(n):
    k = n - 1
    for i in range(n, 0, -1):
        for k in range(1, (i + 1) - 1):
            print(" ", end=" ")
        for j in range(i, n + 1):
            print(j, end=" ")
        print()


pattern_2(5)

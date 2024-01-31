"""
x x x x x x x x x 
  x x x x x x x
    x x x x x
      x x x
        x
"""


def pattern(n):
    for i in range(n, 0, -1):
        for k in range(n, i, -1):
            print(" ", end=" ")

        for j in range(2 * i - 1, 0, -1):
            print("x", end=" ")
        print()


pattern(5)

"""

x x x x x 
  x x x x x
    x x x x x
      x x x x x
        x x x x x

"""


def pattern(n):
    for i in range(1, n + 1):
        for k in range(1, i):
            print(" ", end=" ")

        for j in range(1, n + 1):
            print("x", end=" ")
        print()


pattern(5)

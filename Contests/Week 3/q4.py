"""
x   x   x   x   x   
  x   x   x   x
    x   x   x
      x   x
        x
      x   x
    x   x   x
  x   x   x   x
x   x   x   x   x
"""


def pattern(n):
    for i in range(n, 1, -1):
        for k in range(n, i, -1):
            print(" ", end=" ")
        for j in range(i, 0, -1):
            print("x", end=" ")
            for _ in range(1, 2):
                print(" ", end=" ")
        print()

    for i in range(n + 1, 1, -1):
        for k in range(i - 1, 1, -1):
            print(" ", end=" ")
        for j in range(n + 1, i - 1, -1):
            print("x", end=" ")
            for _ in range(1, 2):
                print(" ", end=" ")

        print()


pattern(5)

"""
        1 
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1

"""


def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, (n + 1) - i):
            print(" ", end=" ")

        for k in range(1, (2 * i) - 1 + 1):
            print(i, end=" ")

        print()

    for i in range(4, 0, -1):
        for j in range(5, i, -1):
            print(" ", end=" ")

        for k in range(i, 3 * i - 1):
            print(i, end=" ")

        print()


pattern(5)

"""
        1 
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1

"""


def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, (n + 1) - i):
            print(" ", end=" ")

        for k in range(1, (2 * i)):
            print(k, end=" ")

        print()

    for i in range(n - 1, 0, -1):
        for j in range(n, i, -1):
            print(" ", end=" ")

        for k in range(1, 2 * (i + 1) - 2):
            print(k, end=" ")

        print()


pattern(5)

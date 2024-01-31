"""
        1 
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1

"""


def pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i):
            print(" ", end=" ")

        for k in range((n + 1) - i, 0, -1):
            print(k, end=" ")

        print()


pattern(5)

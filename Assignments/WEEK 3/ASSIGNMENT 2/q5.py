"""
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""


def pattern(n):
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            print(k, end=" ")

        print()

    for i in range(1, n):
        for k in range(1, (n + 1) - i):
            print(k, end=" ")

        print()


pattern(5)

"""
5 
4 5
3 4 5
2 3 4 5
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5

"""


def pattern(n):
    for i in range(n, 0, -1):
        for k in range(i, n + 1):
            print(k, end=" ")

        print()

    for i in range(1, n):
        for k in range(i + 1, (n + 1)):
            print(k, end=" ")

        print()


pattern(5)

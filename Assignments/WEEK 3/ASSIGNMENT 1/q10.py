"""
1 2 1 2 1 
1 2 1 2
1 2 1
1 2
1

"""


def pattern(n):
    num = 1
    for i in range(n, 0, -1):
        for j in range(n, n - i, -1):
            if j % 2 == 0:
                print(2, end=" ")
            else:
                print(1, end=" ")
        print()


pattern(5)

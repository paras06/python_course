"""
2 22 222 2222 22222 ... upto
n.
(Ask n from user)

"""


def pattern(n: int) -> None:
    i: int = 1
    num: int = 2
    while i <= n:
        print(num, end=" ")
        num = (num * 10) + 2
        i += 1
    print()


def pattern_1(n):
    num = 2
    for i in range(2, n):
        print(num, end=" ")
        num = (num * 10) + 2

    print()


pattern_1(10)

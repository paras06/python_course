"""
Ask x and n from user and then calculate the following answer

"""


def pattern(x: int, y: int) -> int:
    i = 1
    total: int = 0
    num = 1

    while i <= y:
        if i % 2 == 0:
            total = total - x**num
        else:
            total = total + x**num

        num = num + 2

        i = i + 1
    return total


def pattern_1(x: int, y: int) -> int:
    total: int = 0
    num = 1

    for i in range(1, y + 1):
        if i % 2 == 0:
            total = total - x**num
        else:
            total = total + x**num

        num = num + 2
    return total


print(pattern(9, 11))

print(pattern_1(9, 11))

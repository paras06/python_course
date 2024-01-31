# def pattern(n):
#     num = n
#     for i in range(1, 6):
#         for j in range(1, 6):
#             print(j, end=" ")
#         print()


# def pattern(n):
#     num = n
#     for i in range(1, 6):
#         for j in range(1, 6):
#             print(i, end=" ")
#         print()


# def pattern(n):
#     num = n
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")

#         print()


def pattern3(n):
    num = n
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")

        print()


def pattern9(n):
    num = n
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end=" ")

        print()


def pattern1(n):
    num = n
    for i in range(n + 1, 1, -1):
        for j in range(i + 1, 0, -1):
            print(j, end=" ")

        print()


def pattern2(n):
    num = n
    for i in range(n, 0, -1):
        for j in range(n, i - 1, -1):
            print(j, end=" ")
        print()


def pattern(n):
    num = n
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


# def pattern(n):
#     num = n
#     for i in range(1, n + 1):
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()


pattern3(5)
pattern2(5)
pattern1(5)
pattern(5)
pattern3(5)


# def checkPrime(num: int) -> bool:
#     factors = 0
#     i = 1
#     while i <= num:
#         if num % i == 0:
#             factors += 1
#         i += 1
#     if factors == 2:
#         return True
#     else:
#         return False


# def primeInRange(n1, n2):
#     for i in range(n1, n2 + 1):
#         factors = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 factors += 1

#         if factors == 2:
#             print(i, end=" ")


# primeInRange(2, 10)

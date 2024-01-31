# lst = [i for i in range(10, 0, -1)]
# print(lst)


# lst = [i**2 if i % 2 == 0 else i**3 for i in range(1, 20)]
# print(lst)


# original_list = [2, 3.75, 0.04, 59.354, 6, 7.7777, 8, 9]
# only_int = [i for i in original_list if type(i) == int]
# only_float = [i for i in original_list if type(i) == float]

# print(only_int)
# print(only_float)


def isPrime(num: int) -> bool:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


my_list = [i for i in range(1, 51) if isPrime(i) == True]
print(my_list)

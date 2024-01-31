def calc(lst):
    sum = 0
    for i in range(0, len(lst) - 1):
        sum += lst[i]

    return sum


lst = [67, 54, 11, 99, 98, 543, 432, 55.556]
result = calc(lst)
print(result)

"""
Q3. Create a function named multiplicationTable that takes an integer
num as an argument. Print the multiplication table of that number up to 10
numbers

"""


def multiplicationTable(n):
    i = 1

    while i <= 10:
        print(f"{n} * {i} = {n*i}")
        i += 1


multiplicationTable(231)

"""
Create a function countOddEven
that accepts an List of Integers and print how many even and odd numbers are there.

lst = [34, 11, 91, 59, 33, 22]

# Output 
Total even numbers = 2
Total odd numbers = 4

"""


def countOddEven(my_list):
    count_odd, count_even = 0, 0
    for i in my_list:
        if i % 2 == 0:
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1

    print(f"Total even numbers = {count_even}")
    print(f"Total odd numbers = {count_odd}")


lst = [34, 11, 91, 59, 33, 22]
countOddEven(lst)

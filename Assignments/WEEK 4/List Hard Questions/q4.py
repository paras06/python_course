"""
Write a Python code to check if a list is a palindrome (reads the same forwards and backwards). Just print “YES” or “NO”

"""


def palindrome(lst):
    for i in range(0, len(lst) - 1):
        if lst[i] != lst[len(lst) - 1 - i]:
            return False

    return True


my_list = [1, 2, 1, 1, 0, 1, 1, 2, 1]

result = palindrome(my_list)
print("YES") if result else print("NO")

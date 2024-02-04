"""
Create a python function named isPalindrome which accepts a string
as a parameter and return True if its a palindrome. Palindrome are words
which is same when read from start and same when read from the end.

"""


def isPalindrome(str):
    # Method 1
    lower_string = str.lower()
    reversed_string = lower_string[::-1]
    if str.lower() == reversed_string:
        return True
    return False


my_str = "ABCcbaa"
result = isPalindrome(my_str)
print(result)

"""
Ask a string from user. If the length of string is odd, then change all the
capital letters to small and vice versa, but if the length of string is even,
reverse the string. Do this using a function and return the output.


"""


def changeString(str):
    result = ""
    if len(str) % 2 != 0:
        for i in str:
            if i.islower():
                result = result + i.upper()
            else:
                result = result + i.lower()
        return result
    else:
        result = str[::-1]
    return result


user_input = input("Enter a string: ")
print(changeString(user_input))
# str.tol

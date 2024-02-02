"""
Keep asking characters from user.
Until user tpyes quit
Enter character = a
Enter character = b
Enter character = c
Enter character = d
Enter character = d
Enter character = d
Enter character = e
abcddde
"""
# my_string = ""
# while True:
#     char = input("Enter a char = ")
#     if char == "quit":
#         break
#     my_string += char
# print(my_string)


# my_string = "pyTH@#on is GOO!@d"
# result = ""
# for i in my_string:
#     if i.islower() and i.isalpha():
#         result = result + i.upper()
#     elif i.isalpha():
#         result = result + i.lower()

# print(result)


my_string = "pyTHon is *&^GOOd"
result = ""
for i in my_string:
    if i.isupper():
        result += i.lower()
    elif i.islower():
        result += i.upper()
    else:
        result += i
print(result)

"""
Q4.
Don’t create a function, just print the following pattern
1 11 111 1111 11111....n times
(Ask n from user)

"""

num: int = int(input("Enter a number: "))
i = 1
output = ""
while i <= num:
    output = output + "1"
    print(output, end=" ")
    i += 1

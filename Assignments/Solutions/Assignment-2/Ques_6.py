"""
Q6.
Ask 4 numbers from user. Make sure all the numbers entered by user are different. Print which number is the smallest.
"""

num1: int = int(input("Enter a number1: "))
num2: int = int(input("Enter a number2: "))
num3: int = int(input("Enter a number3: "))
num4: int = int(input("Enter a number4: "))

if (
    num1 != num2
    and num1 != num3
    and num1 != num4
    and num2 != num3
    and num2 != num4
    and num3 != num4
):
    smallest_number = min(num1, num2, num3, num4)
    print(f"The smallest number is: {smallest_number}")
else:
    print("Please enter four different numbers.")

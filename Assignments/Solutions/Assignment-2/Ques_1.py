"""
Q1.
Write a program that takes two numbers as input and checks if the first number is divisible by the second.
"""

first_number: int = int(input("Enter the first number: "))
second_number: int = int(input("Enter the Second number: "))

if first_number % second_number == 0:
    print("First number is divisible by second number")
else:
    print("First number is not divisible by second number")

"""
Q5.
Keep asking numbers from user until the user enters
0
. Then display the average of all numbers.

"""

i = 1
sum = 0
count = 0
while True:
    num = int(input("Enter a number (enter 0 to finish): "))
    if num == 0:
        break

    sum += num
    count += 1

print(f"The average of the entered numbers are: {sum/count}")

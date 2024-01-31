"""
armstrongRange

Enter the starting number: 56
Enter the ending number: 1000
Armstrong number between range 56 to 1000 are :
153
370
371
407

"""


def checkArmstrong(n):
    total = 0
    num = n
    while n > 0:
        last_digit = n % 10
        total = total + last_digit**3
        n = n // 10

    if num == total:
        return True
    else:
        return False


def armstrongRange(n1, n2):
    print(f"Armstrong number between range {num1} to {num2} are : ")
    for i in range(n1, n2 + 1):
        if checkArmstrong(i):
            print(i)

    return 0


num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))

result = armstrongRange(num1, num2)

"""
Write a function named notPrimeNumbers which accepts 2 integers n1 and n2.
Print all the numbers from n1 to n2 which are not prime.
Example
notPrimeNumbers(5,20)
6 8 9 10 12 14 15 16 18 20
"""


def isPrime(num: int) -> bool:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


def notPrimeNumbers(n1, n2):
    for i in range(n1, n2 + 1):
        if isPrime(i) == False:
            print(i, end=" ")


num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))

result = notPrimeNumbers(num1, num2)

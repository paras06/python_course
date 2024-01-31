"""
Calculate the cube of all numbers from 1 to a given number

output 
Cube of numbers between range 1 to 25 are :
Cube of number 1 is : 1
Cube of number 2 is : 8
Cube of number 3 is : 27
Cube of number 4 is : 64
Cube of number 5 is : 125
Cube of number 6 is : 216
Cube of number 7 is : 343
Cube of number 8 is : 512
Cube of number 9 is : 729
Cube of number 10 is : 1000
Cube of number 11 is : 1331
Cube of number 12 is : 1728
Cube of number 13 is : 2197
Cube of number 14 is : 2744
Cube of number 15 is : 3375
Cube of number 16 is : 4096
Cube of number 17 is : 4913
Cube of number 18 is : 5832
Cube of number 19 is : 6859
Cube of number 20 is : 8000
Cube of number 21 is : 9261
Cube of number 22 is : 10648
Cube of number 23 is : 12167
Cube of number 24 is : 13824
Cube of number 25 is : 15625
"""


def cube(n):
    for i in range(1, n + 1):
        print(f"Cube of number {i} is : {i**3}")


num1 = int(input("Enter a  number: "))
result = cube(num1)

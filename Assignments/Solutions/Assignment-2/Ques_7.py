"""
Q7.
Take Salary as input from User and Update the salary of an employee.
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment
"""

salary: int = int(input("Enter the salary: "))

if salary <= 10000:
    increment = (salary * 5) / 100
    final_salary = salary + increment
elif salary > 10000 and salary <= 20000:
    increment = (salary * 10) / 100
    final_salary = salary + increment
elif salary > 20000 and salary <= 50000:
    increment = (salary * 15) / 100
    final_salary = salary + increment
elif salary > 50000:
    increment = (salary * 20) / 100
    final_salary = salary + increment
else:
    final_salary = salary

print(f"Your final salary after increment is: {final_salary}")

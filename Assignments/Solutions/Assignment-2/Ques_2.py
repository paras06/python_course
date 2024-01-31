"""
Q2.
A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held
Number of classes attended


1.
Print percentage of class attended
2.
Print Is student is allowed to sit in exam or not

"""

classes_held: int = int(input("Enter the number of classes held: "))
classes_attended: int = int(input("Enter the number of classes attended: "))

attended_percentage = (classes_attended / classes_held) * 100
print(f"Percentage of class attended: {attended_percentage}%")

if attended_percentage < 75:
    print("Student is not allowed to sit in the exam")
else:
    print("Student is allowed to sit in the exam")

# Tuples/ Imutable
# When to use - if the element will not change anytime.

x = (25, 98, 100, 95, 85, 74)


x = list(x)
print(x)

# for i in x:  # by value
#     print(i, end=" ")
# print()

# for i in range(0, len(x)):  # By index
#     print(x[i], end=" ")

# for index, value in enumerate(x):  # by value
#     print(index, value)

# c = x.count(100)
# c = x.index(100)

# # print(x[0])
# print(c)


# x = (25, 98, 100, 95, 85, 74)

# x, y, z = 100, 200, 300

# print(x, y, z)


# Spread OPerator, Splat Operator
# name, gender, age, *marks = ["Anirudh", "Male", 29, 89, 93, 91, 99, 93]
# print(name)
# print(gender)
# print(age)
# print(marks)
*x, y, z = [100, 250, 300, 450, 700, 890]
print(x)
print(y)
print(z)

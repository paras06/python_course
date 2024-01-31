"""
Make two lists of same length and pass it to a function. Return a third
list where each element is the sum of index. Use List Comprehension

"""
import random

lst1 = [random.randint(1, 50) for x in range(12)]
lst2 = [random.randint(-50, 50) for x in range(12)]

print(f"List 1 elements are: {lst1}")
print(f"List 2 elements are: {lst2}")


result = []
lst3 = [result.append(lst1[i] + lst2[i]) for i in range(0, len(lst1))]

print(f"List elements after sum of index are: {result}")

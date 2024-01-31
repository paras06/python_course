"""
Remove duplicates from the list just by using list comprehension.

"""

original_list = [2, 4, 5, 7, 98, 56, 45, 66, 98, 5, 4, 5]

unique_list = []
[unique_list.append(i) for i in original_list if i not in unique_list]
print(unique_list)

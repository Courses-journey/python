"""
Assignment solution
"""
from functools import reduce


my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if  str(item1).isalpha():
        my_data.append(item1)
        last_added = item1


final_string = reduce(lambda a,b:f"{a}{b}",my_data)

print(final_string)

"""
Solve Elzero Assigments
"""
from functools import reduce


my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    a,b = data
    my_data.append(a)
    my_data.append(b)

final_string =reduce(lambda a,b: f"{a}{b}",my_data)
print(final_string)

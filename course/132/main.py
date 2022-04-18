"""
Generate random serial
"""

import string
import random


def generate_serial(count):
    """Generate random serial"""
    char_list =list(string.ascii_letters+string.digits+r"!@#$%^&*()-=+\/")
    char_list_len = len(char_list) -1 
    temp_list = []
    while count > 0:
        # get rand nnum
        rand_num = random.randint(0,char_list_len)
        # get rand char and append it
        temp_list.append(char_list[rand_num])
        # suffele list
        random.shuffle(char_list)
        # to avoid infinte loop
        count -= 1
    return "".join(temp_list)
    # return reduce(lambda a,b : f'{a}{b}',temp_list)

print(generate_serial(20))

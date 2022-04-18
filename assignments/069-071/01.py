values = (0, 1, 2)

# iterate on value list if any value is true
if any(values): # true

  my_var = 0 # local var=0


my_list = [True, 1,  1, ["A", "B"], 10.5, my_var] # my_var none

# True - False - False
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

  print("Good") # Answer is Good

else:

  print("Bad")
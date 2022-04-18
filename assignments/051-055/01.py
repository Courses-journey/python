# Input

my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort()
index = 0
for num in my_nums:
  if num % 5 == 0:
    index += 1
    print(f"{index } => {num}")
else:
  print("All Numbers Printed")
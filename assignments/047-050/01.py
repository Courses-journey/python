num = int(input("Enter the number: "))
count = 0
if num <= 0:
  print("Number must be greater than 0")
else:
  while num > 0:
    num -=1
    if num == 0:
      continue
    if num == 6:
      continue
    print(num) 
    count += 1
  else:
    print(f"{count} Numbers Printed Successfully.")

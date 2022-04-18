num = 1

while num <= 20:
  if num == 6 or num == 8 or num == 12:
    pass
  else:
    print(str(num).zfill(2))
  num += 1
else:
  print("All Numbers Printed")
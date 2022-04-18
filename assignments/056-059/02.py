from unittest import result


def addition(*numbers):
  result = 00
  for num in numbers:
    if num == 10:
      continue
    elif num == 5:
      result -= 5
    else :
      result += num
  else:
    return result

print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160
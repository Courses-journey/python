def my_all(list):
  for num in list:
    if(bool(num)):
      pass
    else :
      return False
  return True

def my_any(list):
  for num in list:
    if(bool(num)):
      return True
    else: 
      pass
  return False

def my_min(list):
  minVal = list[0]
  for num in list:
    if(num < minVal):
      minVal=num
  return minVal

def my_max(list):
  maxVal = list[0]
  for num in list:
    if(num > maxVal):
      maxVal=num
  return maxVal

# my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False

# # my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

# # my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700
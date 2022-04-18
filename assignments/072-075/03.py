from functools import reduce

def numProduct(a,b):
  return a*b

nums = [2, 4, 6, 2]

print(reduce(numProduct,nums))
print(reduce(lambda a,b: a*b,nums))

# Output
96
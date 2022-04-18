def reverse_string(my_string):
  # Your Code Here
  length = len(my_string)-1
  while length >= 0:
    yield my_string[length]
    length -= 1

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)
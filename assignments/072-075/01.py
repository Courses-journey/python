#--------#
#   01   #
#--------#
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

def remove_chars(name):
  return name[1:-1]

for name in map(remove_chars,friends_map):
  print(name)

#--------#
#   02   #
#--------#
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

def remove_chars(name):
  return name[1:-1]

cleaned_list = map(remove_chars,friends_map)
for name in cleaned_list:
  print(name)
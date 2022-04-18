from operator import truediv


#--------#
#   01   #
#--------#
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def get_names(name):
  if(name.endswith("m")):
    return True

for name in filter(get_names,friends_filter):
  print(name)

#--------#
#   02   #
#--------#
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def get_names(name):
  if(name.endswith("m")):
    return True

names = filter(get_names,friends_filter)
for name in names:
  print(name)
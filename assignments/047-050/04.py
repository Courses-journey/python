
my_friends = []

maxCount = 4


index = 0

while maxCount > 0:
  new = input("Friend to add: ").strip()
  if new.isupper():
    print("Invalid Name")
  elif new.islower():
    new.capitalize()
    my_friends.append(new)
    print(f"Friend {new} Added => 1st Letter Become Capital")
    maxCount -= 1
  else:
    new.capitalize()
    my_friends.append(new)
    print(f"Friend {new} Added")
    maxCount -= 1
  print(f"Names Left in List Is {maxCount}")



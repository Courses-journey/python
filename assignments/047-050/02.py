friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
index = 0
count = 0

while index < len(friends):
  if(friends[index][0] == friends[index][0].capitalize()):
    print(friends[index])
  else:
    count += 1
  index += 1
else :
  print(f"Friends Printed And Ignored Names Count Is {count}")

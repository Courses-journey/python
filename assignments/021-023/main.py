# 01
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends.pop(0))
print(friends[-1])
print(friends.pop(-1))

# 02
print("################")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])
print(friends[1::2])

# 03
print("################")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])
print(friends[-2:])

# 04
print("################")

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-2:] = ["Elzero","Elzero"]
print(friends)

# 05
print("################")

friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0,"num 01")
print(friends)
friends.insert(-1,"num 02")
# friends.append("num 02")
print(friends)

# 06
print("################")

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends[0:2] = []
print(friends)
friends[-1:] = []
# friends.pop(-1)
print(friends)

# 07
print("################")

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)

# 08
print("################")

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.reverse()
print(friends)

# 09
print("################")

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))

# 10
print("################")

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
# Needed Output
# Django
print(technologies[4][0])
# Web
print(technologies[4][-1])
from typing import Iterator



#--------#
#   01   #
#--------#

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
filtered = filter(lambda a: not str(a).isdigit(),skills)
for index,skil in enumerate(reversed(list(filtered)),50):
  print(f'"{index} - {skil}"')

#--------#
#   02   #
#--------#
print("#"*50)
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
index = 50
cursor = len(skills)-1
while cursor >= 0:
  if not str(skills[cursor]).isdigit():
    print(f'"{index} - {skills[cursor]}"')
    index += 1
  cursor -= 1

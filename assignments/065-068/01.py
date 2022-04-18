from operator import index
import os

#FIXME need to resolve
desktop_path = r"C:\Users\Eltantawy\OneDrive\Desktop"
newFile = open(f"{desktop_path}\\assign.py","w")

index = 1
# os.mkdir(f"{desktop_path}\Python")
while index <50 :
  newFile = open(f"{desktop_path}\Python\\txt{index}.py","w")
  index += 1

print(os.getcwd())
# print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
print(newFile.name)
print(newFile.name)
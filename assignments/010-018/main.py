# 01
# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt

name , age , country = "Hassan" , 38,"Egypt"

print(f'"Hello \'{name}\', How You Doing \\ """ Your Age Is "{age}"" + And Your Country Is: {country}')

# 02
print("###############")

print(f'"Hello \'{name}\', How You Doing \\\n """ Your Age Is "{age}"" +\n And Your Country Is: {country}')

# 03
print("###############")

name = 'Elzero'
print(f'Second Letter Is "{name[1]}"')
print(f'Third Letter Is "{name[2]}"')
print(f'Last Letter Is "{name[-1]}"')

# 04
print("###############")

print(f'"{name[1:3]}"')
print(f'"{name[::2]}"')
print(f'"{name[::2][::-1]}"')

# 05
print("###############")

name = "#@#@Elzero#@#@"
print(name.strip("#@"))

# 06
print("###############")

num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))

# 07
print("###############")

name_one = "Osama"
name_two = "Osama_Elzero"

# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero

print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

# 08
print("###############")

name_one = "OSamA"
name_two = "osaMA"

# Needed Output
# osAMa
# OSAma
print(name_one.swapcase())
print(name_two.swapcase())

# 09
print("###############")

msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

# 10
print("###############")

name = "Elzero"
print(name.index("z"))

# 11
print("###############")

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love",1))

# 12
print("###############")

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love"))

# 13
print("###############")

name = "Osama"
age = 38
country = "Egypt"

print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")
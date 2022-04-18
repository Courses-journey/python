<div align="center">
<img src="https://elzero.org/wp-content/themes/elzero/imgs/logo.png" alt='source' width="200"/>

# Elzero Web School

[Python Course](https://www.youtube.com/watch?v=mvZHDpCHphk&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs)

</div>

# 006 - Some Data Types Overviews

`type()`
All Data in Python is Object

# 009 - Escape Sequences Characters

`\b` => Back Space
`\newline` => Escape New Line + \
`\\` => Escape Back Slash
`\'` => Escape Single Quotes
`\"` => Escape Double Quotes
`\n` => Line Feed
`\r` => Carriage Return
`\t` => Horizontal Tab
`\xhh` => Character Hex Value

# 012 - Strings Indexing And Slicing

Slicing ( Access Multiple Sequence Items )
`[Start:End]` End Not Included
`[Start:End:Steps]`

- `[:0]` => If Start Is Not Here Will Start From 0
- `[0:]` => If End Is Not Here Will Go To The End
- `[:]` => Full Data
- `[::2]` => take index+2
- `[::-1]` => reverse string

# 013 - Strings Methods Part 1

- `len()` => to get length of element

### trim() equivlent in python

- `.strip()` => to remove spaces at start and end
- `.rstrip()` => to remove spaces at right
- `.lstrip()` => to remove spaces at left
- u can pass string to remove in bracktes eg. `.rstrip("#")` it will remove hashes from right

- `.title()` => to capitlize first char and char after digits
- `.captalize()` => to capitlize

- `.zfill(width)` => to fill string with zero

- `.upper()` => to capitlize each char
- `.lower()` => to make each char lowercase

# 014 - Strings Methods Part 2

- `.split()` => to make each char lowercase by default it split by spaces
  -- u can pass which char to split and how may element to split `.split("-",3)`
- `.rsplit()` => to make each char lowercase by default it split by spaces
  -- u can pass which char to split and how may element to split from right`.rsplit("-",3)`
- `.center(9)` => to center text between by default it center text between space
  -- u can define char to center text between `.center(9,"#")`
- `.count("text")` => to count text in string
  -- u can define range to sreach in `.count("text", 0, 25)`
- `.swapcase()` => to swap char case if upper make it lower
- `.startswith("text")` => check if text start with something
  -- u can define range to sreach in `.startswith("text", 0, 25)`
- `.endswith("text")` => check if text end with something
  -- u can define range to sreach in `.endswith("text", 0, 25)`

# 015 - Strings Methods Part 3

- `.index("text")` => to get index of subText in string
  -- u can define range `index(SubString, Start, End)`
  -- if text dosen't exsist it `return error text not found`
- `.find("text")` => to get index of subText in string
  -- u can define range `find(SubString, Start, End)`
  -- if text dosen't exsist it return `-1`
- `.rjust(Width, Fill Char)` `.ljust(Width, Fill Char)` => work like center
- `.splitlines()` => return lines in list
- `.expandtabs(2)` => control tab between text

### check if text

- `.istitle()` =>
- `.istitle()` =>
- `.islower()` =>
- `.isidentifier()` => check if string can be variable name
- `.isalpha()` => check if string is a-zA-Z
- `.isalnum()` => check if string is alphapetic or number

# 016 - Strings Methods Part 4

- `.replace(Old Value, New Value, Count)` =>
- `"#".join(Iterable)` => join items with `#`

# 017 - Strings Formatting Old Way

### placeholder

- `%s` => String
- `%d` => Number
- `%f` => Float
  -- u can control precsion like `%.2f`

```
n = "Osama"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))
```

### Truncate String | Slice String

- `%.5s` => String control number of char to show

# 018 - Strings Formatting New Ways

### placeholder

- `{:s}` => String
- `{:d}` => Number
  -- u can format money every 3 digit by `{:_d}` | `{:,d}`
  -- not all special char is vaild eg. `{:&d}` is wrong
- `{:f}` => Float
  -- u can control precsion like `{.2f}`

```
n = "Osama"
l = "Python"
y = 10

print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y))
```

### Truncate String | Slice String

- `{.5s}` => String control number of char to show

### ReArrange Items

```
a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two
```

```
x, y, z = 10, 20, 30
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))
```

### Format in Version 3.6+

- `f"{VarName}"`

```
myName = "Osama"
myAge = 36

print("My Name is : {myName} and My Age is : {myAge}")
print(f"My Name is : {myName} and My Age is : {myAge}")
```

# 019 - Numbers

- `myComplexNumber = 5+6j`
  -- `.real` => to print real part of complex
  -- `.imag` => to print imaginary part of complex

- [1] You Can Convert From Int To Float or Complex
- [2] You Can Convert From Float To Int or Complex
- [3] You Cannot Convert Complex To Any Type

- `float(number)` => to convert number to float
- `complex(number)` => to convert number to complex
- `int(number)` => to convert number to int

# 020 - Arithmetic Operators

- `[+]` Addition
- `[-]` Subtraction
- `[*]` Multiplication
- `[/]` Division
- `[%]` Modulus
- `[**]` Exponent
- `[//]` Floor Division

# 021 - Lists

- [1] List Items Are Enclosed in Square Brackets
- [2] List Are Ordered, To Use Index To Access Item
- [3] List Are Mutable => Add, Delete, Edit
- [4] List Items Is Not Unique
- [5] List Can Have Different Data Types

- `list[index]` => to access certin element by index if index grater than length it `return index out of range`
- `list[start:end:step]` => to slice list
- `list[index] = ` => change element value
- `list[start:end:step] = ` => replace slice with lsit ot item

# 022 - Lists Methods Part 1

- `a.append(b)` => add element to the end of the list
  -- if b is a list it will be added to list a as element `list in list`
- `a.extend(b)` => add list elements to list
- `a.remove(element)` => remove first found element from list a
- `.sort()` => to sort list of same type
  -- u can define soert direction by pass reverse to method `.sort(reverse=True)`
- `.reverse()` => reverse list of items

# 023 - Lists Methods Part 2

- `.clear()` => clear all items in list
- `.copy()` => make shallow copy of list
  -- shallow copy => any change made to original list not applied to shallow copy
  -- deep copy => any change made to original list applied to shallow copy
- `.count(item)` => count how many `item` in list
- `.index(item)` => get index of `item` in list
- `.insert(index,item)` => add item to list before given index
- `.pop(index)` => to remove item from given index return value is the deleted item

# 024 - Tuples And Methods Part 1

- [1] Tuple Items Are Enclosed in Parentheses
- [2] You Can Remove The Parentheses If You Want
- [3] Tuple Are Ordered, To Use Index To Access Item
- [4] Tuple Are Immutable => You Cant Add or Delete
- [5] Tuple Items Is Not Unique
- [6] Tuple Can Have Different Data Types
- [7] Operators Used in Strings and Lists Available In Tuples

# 025 - Tuples And Methods Part 2

- Tuple With One Element
  -- to make python know that we have a one element tuple we need to put comma after it

```
myTuple1 = ("Osama",)
myTuple2 = "Osama",
```

- Tuple Concatenation

```
a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b
```

- Tuple, List, String Repeat (\*)

```
myString = "Osama"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)
```

- Tuple Destruct
  -- we use underscore `_` to ignore values

```
a = ("A", "B", 4, "C")

x, y, _, z = a
```

# 026 - Set

- [1] Set Items Are Enclosed in Curly Braces
- [2] Set Items Are Not Ordered And Not Indexed
- [3] Set Indexing and Slicing Cant Be Done
- [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
- [5] Set Items Is Unique

# 027 - Set Methods Part 1

- `.clear()`

- `.union()`

```
  b = {"One", "Two", "Three"}
  c = {"1", "2", "3"}
  x = {"Zero", "Cool"}

print(b | c)
print(b.union(c, x))

```

- `.add()`
- `.copy()`
- `.remove()`

```
g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)
```

- `.discard()`

```
h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
```

- `.pop()`
- `.update()`

```
j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)
```

# 028 - Set Methods Part 2

- `a.difference(b)`
  -- return diffrence between two tupels
  -- equal to `a-b`

```
a = {1, 2, 3, 4}
b = {1, 2, 3, "Osama", "Ahmed"}
print(a.difference(b))  # a - b
```

- `difference_update()`
  -- update orgin set to be the diffrence

```
c = {1, 2, 3, 4}
d = {1, 2, "Osama", "Ahmed"}
c.difference_update(d)  # c - d
```

- `a.intersection(b)`
  -- return similar items between tupels
  -- equal to `a & b`

```
e = {1, 2, 3, 4, "X", "Osama"}
f = {"Osama", "X", 2}
print(e.intersection(f))  # e & f
```

- `a.intersection_update(b)`
  -- update orgin set to be the similar items between tupels

```
g = {1, 2, 3, 4, "X", "Osama"}
h = {"Osama", "X", 2}
g.intersection_update(h)  # g & h
```

- `a.symmetric_difference(b)`
  -- return items not exsist in a and b
  -- equal to `a ^ b`

```
i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4, "X"}
print(i.symmetric_difference(j))  # i ^ j
```

- `a.symmetric_difference_update(b)`
  -- update orgin set to be items not exsist in a and b

```
i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4, "X"}
k.symmetric_difference_update(l)  # k ^ l
```

# 029 - Set Methods Part 3

- `a.issuperset(b)`
  -- check if a is superset of b or all element in b exsist in a
- `a.issubset(b)`
  -- check if a is subset of b or all element in a exsist in b
- `a.isdisjoint(b)`
  -- check if all items in a is diffrent from all items in b

```
g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False
print(g.isdisjoint(i))  # True
```

# 030 - Dictionary

- [1] Dict Items Are Enclosed in Curly Braces
- [2] Dict Items Are Contains Key : Value
- [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
- [4] Dict Value Can Have Any Data Types
- [5] Dict Key Need To Be Unique
  -- if there is repeated key the last one will applied
- [6] Dict Is Not Ordered You Access Its Element With Key

- Accessing values
  -- `dic[key]`
  -- `dic.get(key)`
  -- `dic.keys` => get all key
  -- `dic.values` => get all values

```
user = {
  "name": "Osama",
  "age": 36,
  "country": "Egypt",
  "skills": ["Html", "Css", "JS"],
  "rating": 10.5
}

print(user)
print(user['country'])
print(user.get("country"))
```

- Two-Dimensional Dictionary

```
languages = {
  "One": {
    "name": "Html",
    "progress": "80%"
  },
  "Two": {
    "name": "Css",
    "progress": "90%"
  },
  "Three": {
    "name": "Js",
    "progress": "90%"
  }
}

print(languages)
print(languages['One'])
print(languages['Three']['name'])
```

- `len(dic)` => to get the length of dictionary

# 031 - Dictionary Methods Part 1

- `.clear()`
- `.update({"key": value})` => add new item
  -- u can do the same with `dic[newkey] = newValue`
- `.copy()`
- `.keys()` => return all keys
- `.values()` => return all values

# 032 - Dictionary Methods Part 2

- `a.setdefault(key,value)`
  -- get value of key and assign default value if key not exist in dictionary
  -- if default value not set and key not exsist it return `none`

- `.popitem()`
  -- return the last added number
  -- before v3 it was returning random item

- `.items()` => retun all items in tupels `(key,value)`

- `fromkeys(iterable,value)`

```
a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

print(dict.fromkeys(a, b))
```

# 033 - Boolean

- [1] In Programming You Need to Known Your If Your Code Output is True Or False
- [2] Boolean Values Are The Two Constant Objects False + True.
- all empty object are false `[]` | `()` | `{}` |`""`

# 034 - Boolean Operators

- and
- or
- not

# 035 - Assignment Operators

- `=` =>
- `+=` =>
- `-=` =>
- `*=` =>
- `/=` =>
- `**=` =>
- `%=` =>
- `//=` =>

# 036 - Comparison Operators

- [ == ] Equal
- [ != ] Not Equal
- [ > ] Greater Than
- [ < ] Less Than
- [ >= ] Greater Than Or Equal
- [ <= ] Less Than Or Equal

# 037 - Type Converstion

- `str()`
- `tuple()`
- `list()`
- `set()`
- `dict()` => required list or tuple to be nested with keys and values like
  `(("A",1),("B",6),("C",5))` => Tuples
  `[["A",1],["B",6],["C",5]]` => Lists
  `{{"A",1},{"B",6},{"C",5}}` => Sets

# 038 - User Input

- `input(msg)` => to get input from user

```
fName = input('What\'s Is Your First Name?')
```

# 041 - Control Flow - If, Elif, Else

- `If, Elif, Else`

# 043 - Control Flow - Ternary Conditional Operator

- ` Condition If True | If Condition | Else | Condition If False`

```
print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")
```

# 045 - Membership Operators

- `thing in somethings` => check if thing is included in somethings
- `not in` => check if thing is not included in somethings

# 047 - Loop – While and Else

- `while`
  -- u can use `break` to stop loop

```
# while condition_is_true
#   Code Will Run Until Condition Become False
#   don't forget to put something that end loop
# else:
#   When the ondition_is_false
```

# 051 - Loop – For and Else

- `For`

```
# for item in iterable_object :
#   Do Something With Item
# else:
#   loop is finished
```

- item Is A Vairable You Create and Call Whenever You Want
- item refer to the current position and will run and visit all items to the end
- iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]

# 054 - Break Continue Pass

- `continue` => stop current iteration and go to the next one
- `break` => stop iteration
- `pass` => to use it in empty block which will be implimented later

# 056 - Function and Return

- [1] A Function is A Reusable Block Of Code Do A Task
- [2] A Function Run When You Call It
- [3] A Function Accept Element To Deal With Called [Parameters]
- [4] A Function Can Do The Task Without Returning Data
- [5] A Function Can Return Data After Job is Finished
- [6] A Function Create To Prevent DRY
- [7] A Function Accept Elements When You Call It Called [Arguments]
- [8] There's A Built-In Functions and User Defined Functions
- [9] A Function Is For All Team and All Apps

# 058 - Function Packing, Unpacking Arguments

- must be last param in function arguments if there another argument

```
# define
def say_hello(*peoples):  # n1, n2, n3, n4

  for name in peoples:

    print(f"Hello {name}")

# call
say_hello("Osama", "Ahmed", "Sayed", "Mahmoud")
```

# 059 - Function Default Parameters

- It can be done by assign values to arguments
- Only in last arguments or all arguments

# 060 - Function Packing Unpacking Keyword

- Function Packing, Unpacking Arguments `**KWArgs`

```
def show_skills(*skills):

  print(type(skills))

  for skill in skills:

    print(f"{skill}")

show_skills("Html", "CSS", "JS")

mySkills = {
  'Html': "80%",
  'Css': "70%",
  'Js': "50%",
  'Python': "80%",
  "Go": "40%"
}

def show_skills(**skills):

  print(type(skills))

  for skill, value in skills.items():

    print(f"{skill} => {value}")

show_skills(**mySkills)
```

# 061 - Function Packing Unpacking Arguments

- `**` => to unpack dictionary
- `*` => to unpack tupels

# 062 - Function Scope

- to make local var gloabal we use `global var`

# 063 - Function Recursion

- To Understand Recursion, You Need to First Understand Recursion
- A function that it call it self

```
# Test Word [ WWWoooorrrldd ] # print(x[1:])

def cleanWord(word):

  if len(word) == 1:

    return word

  print(f"Print Start Function {word}")

  if word[0] == word[1]:

    print(f"Print Before Condition {word}")

    return cleanWord(word[1:])

  print(f"Print Before Return {word}")

  return word[0] + cleanWord(word[1:])

  # Stash [ World ]

print(cleanWord("WWWoooorrrldd"))
```

# 064 - Function Lambda

- Anonymous Function
- [1] It Has No Name
- [2] You Can Call It Inline Without Defining It
- [3] You Can Use It In Return Data From Another Function
- [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
- [5] Lambda is One Single Expression not Block Of Code
- [6] Lambda Type is Function

```
def say_hello(name, age) : return f"Hello {name} your Age Is: {age}"
print(say_hello("Ahmed", 36))
```

```
hello = lambda name, age : f"Hello {name} your Age Is: {age}"
print(hello("Ahmed", 36))
```

- U can get method or function name by using `__name__`

# 065 - Files Handling – Part 1 Intro

- file modes
  -- `"a"` Append Open File For Appending Values, Create File If Not Exists
  -- `"r"` Read [Default Value] Open File For Read and Give Error If File is Not Exists
  -- `"w"` Write Open File For Writing, Create File If Not Exists
  -- `"x"` Create Create File, Give Error If File Exists

- `open(path,mode)`
  - path can be relative or absolute
  - mode can be any from above

```
import os

# Main Current Working Directory
print(os.getcwd())

# Directory For The Opened File
print(os.path.dirname(os.path.abspath(__file__)))

# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

print(os.path.abspath(__file__))

file = open(r"D:\Python\Files\nfiles\osama.txt")

file = open("D:\Python\Files\osama.txt")
```

- To make string ignore every special char and make it a raw string u must put `r` before quotes `r"this is raw text and this \n won't work"`

# 066 - Files Handling Part 2 Read Files

- By default when print file it give u data about it not the containing content

```
myFile = open("D:\Python\Files\osama.txt", "r")

print(myFile)  # File Data Object
```

- U can access certin data like that

```
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)
```

- To read content use `read()`
  -- u can define bytes to read
  -- by default bytes is set to `-1` mean get all content

```
print(myFile.read())
print(myFile.read(5))
```

- `readline()` used to get content from line
  -- u can specify bytes to read from this line
  -- if u called it again it will read the next line

```
print(myFile.readline(5))
print(myFile.readline())
print(myFile.readline())

print(myFile.readlines())
print(myFile.readlines(50))
```

- `readlines` to get all lines as a list

```
print(type(myFile.readlines()))

for line in myFile:

  print(line)

  if line.startswith("07"):

    break

```

- Best paractise is to close file after finishing ur stuff

```
# Close The File

myFile.close()
```

# 067 - Files Handling Part 3 Write and Append In Files

```
myFile = open("D:\Python\Files\osama.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"D:\Python\Files\fun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open("D:\Python\Files\osama.txt", "w")
myFile.writelines(myList)

myFile = open("D:\Python\Files\osama.txt", "a")
myFile.write("Elzero")
```

# 068 - Files Handling – Part 4 Important Info

- `truncate(bytes)` =>

```
myFile = open("D:\Python\Files\osama.txt", "a")
myFile.truncate(5)
```

- `tell()` => get cursor postion
  -- new line in windows calculate as two bytes

```
myFile = open("D:\Python\Files\osama.txt", "a")
print(myFile.tell())
```

- `seek(bytes)` => set cursor postion

```
myFile = open("D:\Python\Files\osama.txt", "r")
myFile.seek(11)
print(myFile.read())
```

- `remove(path)` => remove

```
os.remove("D:\Python\Files\osama.txt")
```

# 069 - Built In Functions Part 1

- `all(iterable)` => Check if all items in iterable are true then return true
- `any(iterable)` => Check if any item in iterable are true then return true
- `bin(5532)` => Convert to binary
- `id(var)` => Get id or iddress of var in memory

# 070 - Built In Functions Part 2

- `sum(iterable,start)` => Get sum of all items in iterable
- `round(num,percision = 0)` => Round flaoting number
- `range(start = 0,end,step = 1)` => Get range of number
- `print()` => print to console
  -- `sep=" "` => to define separtor between text when there is too many args to be printed by default it's add space
  -- `end="\n"` => to define end of text by default it add new ;ine

# 071 - Built In Functions Part 3

- `abs()` => get the absolute value of number
- `pow(number,exponent)` => equal to `number**exp`
- `min(iteratable)` => Get min from list
- `max(iteratable)` => Get max value from list
- `a[slice(start,end ,step)]` => Same as `a[start:end:stop]` but stop must write

# 072 - Built In Functions Part 4 – Map

- [1] Map Take A Function + Iterator
- [2] Map Called Map Because It Map The Function On Every Element
- [3] The Function Can Be Pre-Defined Function or Lambda Function

- Use Map With Predefined Function

```
def formatText(text):

  return f"- {text.strip().capitalize()} -"

myTexts = [" OSama ", "AHMED", "  sAYed  "]

myFormatedData = map(formatText, myTexts)

print(myFormatedData)

for name in list(map(formatText, myTexts)):

  print(name)

print("#" * 50)
```

- Use Map With Lambda Function

```
def formatText(text):

  return f"- {text.strip().capitalize()} -"

myTexts = [" OSama ", "AHMED", "  sAYed  "]

for name in list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts)):

  print(name)
```

# 073 - Built In Functions Part 5 – Filter

- [1] Filter Take A Function + Iterator
- [2] Filter Run A Function On Every Element
- [3] The Function Can Be Pre-Defined Function or Lambda Function
- [4] Filter Out All Elements For Which The Function Return True
- [5] The Function Need To Return Boolean Value

- Example 1

```
def checkNumber(num):

  return num > 10

myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

myResult = filter(checkNumber, myNumbers)

for number in myResult:

  print(number)

print("#" * 50)
```

- Example 2

```
def checkName(name):

  return name.startswith("O")

myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

myReturnedData = filter(checkName, myTexts)

for person in myReturnedData:

  print(person)

print("#" * 50)
```

- Example 3

```
myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]

for p in filter(lambda name: name.startswith("A"), myNames):

  print(p)
```

# 074 - Built In Functions Part 6 – Reduce

- [1] Reduce Take A Function + Iterator
- [2] Reduce Run A Function On FIrst and Second Element And Give Result
- [3] Then Run Function On Result And Third Element
- [4] Then Run Function On Rsult And Fourth Element And So On
- [5] Till One ELement is Left And This is The Result of The Reduce
- [6] The Function Can Be Pre-Defined Function or Lambda Function

```
from functools import reduce

def sumAll(num1, num2):

  return num1 + num2

numbers = [1, 8, 2, 9, 100]

result = reduce(sumAll, numbers)

result = reduce(lambda num1, num2: num1 + num2, numbers)

print(result)

# ((((1 + 8) + 2) + 9) + 100)
```

# 075 - Built In Functions Part 7

- `enumerate(iterable, start=0)` => add counter to itertable

```
mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 20)

print(type(mySkillsWithCounter))

for counter, skill in mySkillsWithCounter:

  print(f"{counter} - {skill}")

print("#" * 50)
```

- `help()` => Get the manual of any function in python

```
print(help(print))

print("#" * 50)
```

- `reversed(iterable)` => Return reversed oreder iteratable

```
myString = "Elzero"

print(reversed(myString))

for letter in reversed(myString):

  print(letter)

for s in reversed(mySkills):

  print(s)
```

# 076 - Modules Part 1 - Intro And Built In Modules

- [1] Module is A File Contain A Set Of Functions
- [2] You Can Import Module in Your App To Help You
- [3] You Can Import Multiple Modules
- [4] You Can Create Your Own Modules
- [5] Modules Saves Your Time

- Import Main Module

```
import random
print(random)
print(f"Print Random Float Number {random.random()}")
```

- Show All Functions Inside Module

```
print(dir(random))
```

- Import One Or Two Functions From Module

```
from random import randint, random
print(f"Print Random Float {random()}")
print(f"Print Random Integer {randint(100, 900)}")
```

# 077 - Modules – Part 2 – Create Your Module

- Add path to import module from

```
import sys
sys.path.append(r"D:\Games")
print(sys.path)
```

- Import ur own module and use it
  -- `dir(module)` => to list all method included

```
import elzero
print(dir(elzero))

elzero.sayHello("Ahmed")

elzero.sayHowAreYou("Ahmed")
```

- Alias => give ur module shorten name or an alias
  -- can be make to module name or function in it

```
import elzero as ee

ee.sayHello("Ahmed")

ee.sayHowAreYou("Ahmed")
```

```
from elzero import sayHello

sayHello("Osama")

from elzero import sayHello as ss

ss("Osama")
```

- To solve problem of import in vscode `cntrl`+`shift`+`P`
  -- open `settings` json file
  -- add `"python.autocomplete.extraPaths":["path"]`

# 078 - Modules – Part 3 – Install External Packages

- [1] Module vs Package
- [2] External Packages Downloaded From The Internet
- [3] You Can Install Packages With Python Package Manager PIP
- [4] PIP Install the Package and Its Dependencies
- [5] Modules List "https://docs.python.org/3/py-modindex.html"
- [6] Packages and Modules Directory "https://pypi.org/"
- [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"

- `pip --version` => To check if `pip` is installed
- `pip list` => List all installed packages or modules and its version
- `pip install pakageName` => Install package or module
  -- u can write all pakages `pip install pakageName01 pakageName02 pakageName03 ...`
  -- `packName==versio` => Specify certin version
  -- `packName>=versio` => Specify any version above this version

- `pyfiglet` => String to ASCI art
- `termcolor` => Color string in console

```
import termcolor
import pyfiglet

print(dir(pyfiglet))
print(pyfiglet.figlet_format("Elzero"))
print(termcolor.colored("Elzero", color="yellow"))

print(termcolor.colored(pyfiglet.figlet_format("Elzero"), color="yellow"))
```

# 079 - Date And Time Introduction

```
import datetime
```

```
# print(dir(datetime))
# print(dir(datetime.datetime))
```

```
# Print The Current Date and Time
print(datetime.datetime.now())

print("#" * 40)

# Print The Current Year
print(datetime.datetime.now().year)

# Print The Current Month
print(datetime.datetime.now().month)

# Print The Current Day
print(datetime.datetime.now().day)

print("#" * 40)
```

- Print Start and End Of Date

```
print(datetime.datetime.min)
print(datetime.datetime.max)

print("#" * 40)

# print(dir(datetime.datetime.now()))
```

- Print The Current Time

```
print(datetime.datetime.now().time())

print("#" * 40)
```

- Print The Current Time Hour

```
print(datetime.datetime.now().time().hour)
```

- Print The Current Time Minute

```
print(datetime.datetime.now().time().minute)
```

- Print The Current Time Second

```
print(datetime.datetime.now().time().second)

print("#" * 40)
```

- Print Start and End Of Time

```
print(datetime.time.min)
print(datetime.time.max)

print("#" * 40)
```

- Print Specific Date

```
print(datetime.datetime(1982, 10, 25))
print(datetime.datetime(1982, 10, 25, 10, 45, 55, 150364))
```

```
myBirthDay = datetime.datetime(1982, 10, 25)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} And ", end="")
print(f"Date Now Is {dateNow}")

print(f" I Lived For {dateNow - myBirthDay}")
print(f" I Lived For {(dateNow - myBirthDay).days} Days.")
```

# 080 - Date And Time Format Date

- https://strftime.org/

```
import datetime
```

```
myBirthday = datetime.datetime(1982, 10, 25)

print(myBirthday)
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))

print(myBirthday.strftime("%d %B %Y"))
print(myBirthday.strftime("%d, %B, %Y"))
print(myBirthday.strftime("%d/%B/%Y"))
print(myBirthday.strftime("%d - %B - %Y"))
print(myBirthday.strftime("%B - %Y"))

```

# 081 - Iterable Vs Iterator

- Iterable
  -- [1] Object Contains Data That Can Be Iterated Upon
  -- [2] Examples (String, List, Set, Tuple, Dictionary)

- Iterator
  -- [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
  -- [2] You Can Generate Iterator From Iterable When Using iter() Method
  -- [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
  -- [4] Gives "StopIteration" If Theres No Next Element

```
myString = "Osama"

myList = [1, 2, 3, 4, 5]

for letter in myString:

  print(letter, end=" ")

for number in myList:

  print(number, end=" ")

myIterator = iter(myString)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

for letter in iter("Elzero"):

  print(letter, end=" ")
```

# 082 - Generators

- [1] Generator is a Function With "yield" Keyword Instead of "return"
- [2] It Support Iteration and Return Generator Iterator By Calling "yield"
- [3] Generator Function Can Have one or More "yield"
- [4] By Using next() It Resume From Where It Called "yield" Not From Begining
- [5] When Called, Its Not Start Automatically, Its Only Give You The Control

```
def myGenerator():
  yield 1
  yield 2
  yield 3
  yield 4

myGen = myGenerator()

print(next(myGen), end=" ")
print("Hello From Python")
print(next(myGen), end=" ")

for number in myGen:
  print(number)
```

# 083 - Decorators – Intro

- [1] Sometimes Called Meta Programming
- [2] Everything in Python is Object Even Functions
- [3] Decorator Take A Function and Add Some Functionality and Return It
- [4] Decorator Wrap Other Function and Enhance Their Behaviour
- [5] Decorator is Higher Order Function (Function Accept Function As Parameter)

```
def myDecorator(func):  # Decorator

  def nestedFunc():  # Any Name Its Just For Decoration

    print("Before")  # Message From Decorator

    func()  # Execute Function

    print("After")  # Message From Decorator

  return nestedFunc  # Return All Data
```

- Sugar syntax `recommended`

```
@myDecorator

def sayHello():

  print("Hello From Say Hello Function")

sayHello()
```

```
@myDecorator

def sayHowAreYou():

  print("Hello From Say How Are You Function")

sayHowAreYou()
```

- replace for sugar format

```
afterDecoration = myDecorator(sayHello)

afterDecoration()
```

# 085 - Decorators – Function with Parameters

- Function accept one or more decoration

```
def myDecorator(func):  # Decorator

  def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

    if num1 < 0 or num2 < 0:

      print("Beware One Of The Numbers Is Less Than Zero")

    func(num1, num2)  # Execute Function

  return nestedFunc  # Return All Data

def myDecoratorTwo(func):  # Decorator

  def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

    print("Coming From Decorator Two")

    func(num1, num2)  # Execute Function

  return nestedFunc  # Return All Data
```

```
@myDecorator
@myDecoratorTwo

def calculate(n1, n2):

  print(n1 + n2)

calculate(-5, 90)
```

# 086 - Practical Loop on Many Iterators With Zip

- zip() Return A Zip Object Contains All Objects
- zip() Length Is The Length of Lowest Object

```
list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"]
tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {"Name": "Osama", "Age": 36, "Country": "Egypt", "Skill": "Python"}

for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):

  print("List 1 Item =>", item1)
  print("List 2 Item =>", item2)
  print("Tuple 1 Item =>", item3)
  print("Dict 1 Key =>", item4, "Value =>", dict1[item4])

ultimateList = zip(list1, list2)
print(ultimateList)
for item in ultimateList:
  print(item)
```

# 087 - Practical Image Manipulation With Pillow

```
from PIL import Image

# Open The Image
myImage = Image.open("D:\Python\Files\game.jpg")

# Show The Image
myImage.show()

# My Cropped Image
myBox = (300, 300, 800, 800)
myNewImage = myImage.crop(myBox)

# Show The New Image
myNewImage.show()

# My Converted Mode Image
myConverted = myImage.convert("L")
myConverted.show()
```

# 088 - Doc String & Commenting vs Documenting

- [1] Documentation String For Class, Module or Function
- [2] Can Be Accessed From The Help and Doc Attributes
- [3] Made For Understanding The Functionality of The Complex Code
- [4] Theres One Line and Multiple Line Doc Strings

- Single Line doc

```
def elzero_function(name):
  ''' DOC Text  '''
  print(f"Hello {name} From Elzero")
```

- MultiLine doc

```
def elzero_function(name):
  """
  Elzero Function
    It Say Hello From Elzero
  Parameter:
    name => Person Name That Use Function
  Return:
    Return Hello Message To The Person
  """
  print(f"Hello {name} From Elzero")
```

```
elzero_function("Ahmed")

print(dir(elzero_function))

print(elzero_function.__doc__)

help(elzero_function)
```

# 089 - Installing And Use Pylint For Better Code

- `pip install pylint`
- [Vscode extension](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)

- In Terminal `pylint.exe fileLocation`
  -- eg. `pylint.exe d:/python/main.py`

# 090 - Errors And Exceptions Raising

- [1] Exceptions Is A Runtime Error Reporting Mechanism
- [2] Exception Gives You The Message To Understand The Problem
- [3] Traceback Gives You The Line To Look For The Code in This Line
- [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
- [5] [Exceptions List](https://docs.python.org/3/library/exceptions.html)
- [6] raise Keyword Used To Raise Your Own Exceptions

```
x = -10

if x < 0:

  raise Exception(f"The Number {x} Is Less Than Zero")

  print("This Will Not Print Because The Error")

else:

  print(f"{x} Is Good Number and Ok")

print('Print Message After If Condition')

y = 10

if type(y) != int:

  raise ValueError("Only Numbers Allowed")

print('Print Message After If Condition')
```

# 091 - Exceptions Handling Try, Except, Else, Finally

- `Try` => Test The Code For Errors
- `Except` => Handle The Errors
- `Else` => If No Errors
- `Finally` => Run The Code

```
number = int(input("Write Your Age: "))

print(number)
print(type(number))

try:  # Try The Code and Test Errors

  number = int(input("Write Your Age: "))

  print("Good, This Is Integer From Try")

except:  # Handle The Errors If Its Found

  print("Bad, This is Not Integer")

else:  # If Theres No Errors

  print("Good, This Is Integer From Else")

finally:

  print("Print From Finally Whatever Happens")


try:

  # print(10 / 0)
  # print(x)
  print(int("Hello"))

except ZeroDivisionError:

  print("Cant Divide")

except NameError:

  print("Identifier Not Found")

except ValueError:

  print("Value Error Elzero")

except:

  print("Error Happens")
```

# 093 - Debugging Code

```
my_list = [1, 2, 3]

my_dictionary = {"Name": "Osama", "Age": 36, "Country": "Egypt"}

for num in my_list:

  print(num)

for key, value in my_dictionary.items():

  print(f"{key} => {value}")

def function_one_one():

  print("Hello From Function One")

function_one_one()
```

# 094 - Type Hinting

- It's just a type hint for your code
- Not affect code or put restrict in runtime to var

- `var : type`
- `def funNamr() -> type:`

```
def say_hello(name) -> str:

  print(f"Hello {name}")

say_hello("Ahmed")

def calculate(n1, n2) -> str:

  print(n1 + n2)

calculate(10, 40)
```

# 095 - Regular Expressions Part 1 Intro

- [1] Sequence of Characters That Define A Search Pattern
- [2] Regular Expression is Not In Python Its General Concept
- [3] Used In [Credit Card Validation, IP Address Validation, Email Validation]
- [4] [Test RegEx]("https://pythex.org/")
- [5] [Characters Sheet]("https://www.debuggex.com/cheatsheet/regex/python")

# 096 - Regular Expressions Part 2 Quantifiers

- `*` 0 or more
- `+` 1 or more
- `?` 0 or 1
- `{2}` Exactly 2
- `{2, 5}` Between 2 and 5
- `{2,}` 2 or more
- `(,5}` Up to 5

- [regex101](https://regex101.com/)

# 098 - Regular Expressions Part 4 Assertions & Email Pattern

- `^` Start of String
- `$` End of string

```
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$
```

# 99 - Regular Expressions Part 5 Logical Or And Escaping

- `|` Or
- `\` Escape Special Characters
- `()` Separate Groups

# 100 - Regular Expressions Part 6 Re Module Search And FindAll

- search() => Search A String For A Match And Return A First Match Only
- findall() => Returns A List Of All Matches and Empty List if No Match
- Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)

- `.span()` is postion of searched string
- `.match` is the searched string
- `.string` is the string u search into
- `.group()`

```
import re
```

```
my_search = re.search(r"[A-Z]{2}", "OOsamaEElzero")

print(my_search)
print(my_search.span())
print(my_search.string)
print(my_search.group())

is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@osama.com")

if is_email:

  print("This is A Valid Email")

  print(is_email.span())
  print(is_email.string)
  print(is_email.group())

else:

  print("This is Not A Valid Email")
```

```
email_input = input("Please Write Your Email: ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

empty_list = []

if search != []:

  empty_list.append(search)

  print("Email Added")

else:

  print("Invalid Email")

for email in empty_list:

  print(email)
```

# 101 - Regular Expressions Part 7 Re Module Split And Sub

- `split(Pattern, String, MaxSplit)` => Return A List Of Elements Splitted On Each Match
- `sub(Pattern, Replace, String, ReplaceCount)` => Replace Matches With What You Want

```
import re
```

```
string_one = "I Love Python Programming Language"

search_one = re.split(r"\s", string_one, 1)

print(search_one)

print("#" * 50)

string_two = "How-To_Write_A_Very-Good-Article"

search_two = re.split(r"-|_", string_two)

print(search_two)

print("#" * 50)

# Get Words From URL

for counter, word in enumerate(search_two, 1):

  if len(word) == 1:

    continue

  print(f"Word Number: {counter} => {word.lower()}")

print("#" * 50)

my_string = "I Love Python"

print(re.sub(r"\s", "-", my_string, 1))
```

# 102 - Regular Expressions Part 8 Group Trainings And Flags

- `.group()` => return matched string grouped as one word
- `.groups()` => return matched string in group
  -- if the group regx not exsist it returns `none`

- Flags
  -- ignorecase
  -- multiline
  -- notall
  -- notall
  -- verbose

# 103 - OOP – Part 1 Intro

- [1] Python Support Object Oriented Programming
- [2] OOP Is A Paradigm Or Coding Style
  OOP Paradigm =>
  Means Structuring Program So The Methods[Functions] and Attributes[Data]
  Are Bundled Into Objects
- [3] Methods => Act As Function That Use The Information Of The Object
- [4] Python Is Multi-Paradigm Programming Language [Procedural, OOP, Functional]
  -- Procedural => Structure App Like Recipe, Sets Of Steps To Make The Task
  -- Functional => Built On the Concept of Mathematical Functions
- [5] OOP Allow You To Organize Your Code and Make It Readable and Reusable
- [6] Everything in Python is Object
- [7] If Man Is Object
  -- Attributes => Name, Age, Address, Phone Number, Info [Can Be Differnet]
  -- Methods[Behaviors] => Walking, Eating, Singing, Playing
- [8] If Car Is Object
  -- Attributes => Model, Colour, Price
  -- Methods[Behaviors] => Walking, Stopping
- [9] Class Is The Template For Creating Objects [Object Constructor | Blueprint]
  -- Class Car Can Create Many Cars Object

# 104 - OOP – Part 2 Class Syntax And Info

- [01] Class is The Blueprint Or Construtor Of The Object
- [02] Class Instantiate Means Create Instance of A Class
- [03] Instance => Object Created From Class And Have Their Methods and Attributes
- [04] Class Defined With Keyword class
- [05] Class Name Written With PascalCase [UpperCamelCase] Style
- [06] Class May Contains Methods and Attributes
- [07] When Creating Object Python Look For The Built In **init** Method
- [08] `__init__` Method Called Every Time You Create Object From Class
- [09] `__init__` Method Is Initialize The Data For The Object
- [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
- [11] self Refer To The Current Instance Created From The Class And Must Be First Param
- [12] self Can Be Named Anything
- [13] In Python You Dont Need To Call new() Keyword To Create Object

- any word with two underscoer `__` called dander method or magic method

```
# Syntax
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function
```

# 105 - OOP – Part 3 Instance Attributes and Methods Part 1

- Self: Point To Instance Created From Class
- Instance Attributes: Instance Attributes Defined Inside The Constructor
- Instance Methods: Take Self Parameter Which Point To Instance Created From Class
- Instance Methods Can Have More Than One Parameter Like Any Function
- Instance Methods Can Freely Access Attributes And Methods On The Same Object
- Instance Methods Can Access The Class Itself

```
class Member:
  def __init__(self, first_name, middle_name, last_name):
    self.fname = first_name
    self.mname = middle_name
    self.lname = last_name

member_one = Member("Osama", "Mohamed", "Elsayed")
member_two = Member("Ahmed", "Ali", "Mahmoud")
member_three = Member("Mona", "Ali", "Mahmoud")

# print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname)
print(member_three.fname)
```

# 106 - OOP – Part 4 Instance Attributes and Methods Part 2

```
class Member:
  def __init__(self, first_name, middle_name, last_name, gender):
    self.fname = first_name
    self.mname = middle_name
    self.lname = last_name
    self.gender = gender

  def full_name(self):
    return f"{self.fname} {self.mname} {self.lname}"

  def name_with_title(self):
    if self.gender == "Male":
      return f"Hello Mr {self.fname}"
    elif self.gender == "Female":
      return f"Hello Miss {self.fname}"
    else:
      return f"Hello {self.fname}"

  def get_all_info(self):
    return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"


member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")

# print(dir(member_one))

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.fname)
# print(member_three.fname)

# print(member_two.full_name())
# print(member_two.name_with_title())

print(member_one.get_all_info())
```

# 107 - OOP – Part 5 Class Attributes

- Instance attributes exist in `__main__`
  -- use `self` to refrenece it
- Class attributes exist in class itself
  -- use `className` to refrenece it

```
class Member:

  not_allowed_names = ["Hell", "Shit", "Baloot"]

  users_num = 0

  def __init__(self, first_name, middle_name, last_name, gender):

    self.fname = first_name

    self.mname = middle_name

    self.lname = last_name

    self.gender = gender

    Member.users_num += 1  # Member.users_num = Member.users_num + 1

  def full_name(self):

    if self.fname in Member.not_allowed_names:

      raise ValueError("Name Not Allowed")

    else:

      return f"{self.fname} {self.mname} {self.lname}"

  def name_with_title(self):

    if self.gender == "Male":

      return f"Hello Mr {self.fname}"

    elif self.gender == "Female":

      return f"Hello Miss {self.fname}"

    else:

      return f"Hello {self.fname}"

  def get_all_info(self):

    return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

  def delete_user(self):

    Member.users_num -= 1  # Member.users_num = Member.users_num -1

    return f"User {self.fname} Is Deleted."


print(Member.users_num)

member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")
member_four = Member("Shit", "Hell", "Metal", "DD")

print(Member.users_num)

print(member_four.delete_user())

print(Member.users_num)

print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname)
print(member_three.fname)

print(member_two.full_name())
print(member_two.name_with_title())

print(member_three.get_all_info())

print(dir(Member))
```

# 108 - OOP – Part 6 Class Methods and Static Methods

- Class Methods:
  -- Marked With `@classmethod` Decorator To Flag It As Class Method
  -- It Take `Cls` Parameter Not `Self` To Point To The Class not The Instance
  -- It Doesn't Require Creation of a Class Instance
  -- Used When You Want To Do Something With The Class Itself

- Static Methods:
  -- Marked With `@staticmethod` Decorator To Flag It As Class Method
  -- It Takes No Parameters
  -- Its Bound To The Class Not Instance
  -- Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class

```
print(member_one.full_name())
print(Member.full_name(member_one))
```

# 109 - OOP – Part 7 Class Magic Methods

-- Everything in Python is An Object

- `__init__` Called Automatically When Instantiating Class
- `self.__class__` The class to which a class instance belongs
- `__str__` Gives a Human-Readable Output of the Object
  -- Called When We Use the `print()` Function on the Object
- `__len__` Returns the Length of the Container
  -- Called When We Use the Built-in `len()` Function on the Object

```
class Skill:

  def __init__(self):

    self.skills = ["Html", "Css", "Js"]

  def __str__(self):

    return f"This is My Skills => {self.skills}"

  def __len__(self):

    return len(self.skills)

profile = Skill()
print(profile)
print(len(profile))

profile.skills.append("PHP")
profile.skills.append("MySQL")

print(len(profile))

print(profile.__class__)
my_string = "Osama"
print(type(my_string))
print(my_string.__class__)
print(dir(str))
print(str.upper(my_string))
```

# 110 - OOP – Part 8 Inheritance

```
class Food:  # Base Class

  def __init__(self, name, price):

    self.name = name

    self.price = price

    print(f"{self.name} Is Created From Base Class")

  def eat(self):

    print("Eat Method From Base Class")

class Apple(Food):  # Derived Class

  def __init__(self, name, price, amount):

    # Food.__init__(self, name)  # Create Instance From Base Class

    super().__init__(name, price)

    self.amount = amount

    print(f"{self.name} Is Created From Derived Class And Price Is {self.price} And Amount Is {self.amount}")

  def get_from_tree(self):

      print("Get From Tree From Derived Class")

# food_one = Food("Pizza")
food_two = Apple("Pizza", 150, 500)
food_two.eat()
food_two.get_from_tree()
```

# 111 - OOP – Part 9 Multiple Inheritance & Methods Override

- MRO => Method Resultion Order => order of class and its parents
  -- `.mro`

```
class BaseOne:

  def __init__(self):

    print("Base One")

  def func_one(self):

    print("One")

class BaseTwo:

  def __init__(self):

    print("Base Two")

  def func_two(self):

    print("Two")

class Derived(BaseOne, BaseTwo):

  pass

my_var = Derived()

# print(Derived.mro())

print(my_var.func_one)
print(my_var.func_two)

my_var.func_one()
my_var.func_two()

class Base:

  pass

class DerivedOne(Base):

  pass

class DerivedTwo(DerivedOne):

  pass
```

# 112 - OOP Part 10 - Polymorphism

- Double face method

- U can make method required to be implemented in child or derived calsses by writing `raise NotImplementedError("Text to show)`

```
n1 = 10
n2 = 20

print(n1 + n2)

s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2)

print(len([1, 2, 3, 4, 5, 6]))
print(len("Osama Elzero"))
print(len({"Key_One": 1, "Key_Two": 2}))

class A:

  def do_something(self):

    print("From Class A")

    raise NotImplementedError("Derived Class Must Implement This Method")

class B(A):

  def do_something(self):

    print("From Class B")

class C(A):

  def do_something(self):

    print("From Class C")

my_instance = B()
my_instance.do_something()
```

# 113 - OOP – Part 11 Encapsulation

- Encapsulation
  -- Restrict Access To The Data Stored in Attirbutes and Methods

- Public
  -- Every Attribute and Method That We Used So Far Is Public
  -- Attributes and Methods Can Be Modified and Run From Everywhere
  -- Inside Our Outside The Class

- Protected
  -- Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
  -- Attributes and Methods Prefixed With One Underscore `_`
  -- Python dosen't support that but the `_` to tell U and developer that this thing mustn't accessed
  -- `print(one._name)`
- Private
  -- Attributes and Methods Can Be Accessed From Within The Class Or Object Only
  -- Attributes Cannot Be Modified From Outside The Class
  -- Attributes and Methods Prefixed With Two Underscores `__`
  -- Python dosen't support that but the `_` to tell U and developers that this thing mustn't accessed
  -- `print(var._ClassOfVar_privateVar)`

- `Attributes = Variables = Properties`

```
class Member:

  def __init__(self, name):

    self.name = name  # Public

one = Member("Ahmed")
print(one.name)
one.name = "Sayed"
print(one.name)

class Member:

  def __init__(self, name):

    self._name = name  # Protected

one = Member("Ahmed")
print(one._name)
one._name = "Sayed"
print(one._name)

class Member:

  def __init__(self, name):

    self.__name = name  # Private

  def say_hello(self):

    return f"Hello {self.__name}"

one = Member("Ahmed")
# print(one.__name)
print(one.say_hello())
print(one._Member__name)
```

# 114 - OOP Part 12 Getters And Setters

```
class Member:

  def __init__(self, name):

    self.__name = name  # Private

  def say_hello(self):

    return f"Hello {self.__name}"

  def get_name(self):  # Getter

    return self.__name

  def set_name(self, new_name):

    self.__name = new_name

one = Member("Ahmed")

one._Member__name = "Sayed"
print(one._Member__name)

print(one.get_name())
one.set_name('Abbas')
print(one.get_name())
```

# 115 - OOP – Part 13 @Property Decorator

- Any Method dosn't required any param and return values u can use `@Property` Decorator to use it like properties

```
class Member:

  def __init__(self, name, age):

    self.name = name

    self.age = age

  def say_hello(self):

    return f"Hello {self.name}"

  @property
  def age_in_days(self):

    return self.age * 365

one = Member("Ahmed", 40)

print(one.name)
print(one.age)
print(one.say_hello())
# print(one.age_in_days())

print(one.age_in_days)
```

# 116 - OOP – Part 14 ABC Abstract Base Class

- Class Called Abstract Class If it Has One or More Abstract Methods
- abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
- By Adding @absttractmethod Decorator on The Methods
- ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class

```
from abc import ABCMeta, abstractmethod

class Programming(metaclass=ABCMeta):

  @abstractmethod
  def has_oop(self):

    pass

  @abstractmethod
  def has_name(self):

    pass

class Python(Programming):

  def has_oop(self):

    return "Yes"

class Pascal(Programming):

  def has_oop(self):

    return "No"

  def has_name(self):

    return "Pascal"

one = Pascal()

print(one.has_oop())
print(one.has_name())
```

# 117 - Databases – Intro About Databases

- Database Is A Place Where We Can Store Data
- Database Organized Into Tables (Users, Categories)
- Tables Has Columns (ID, Username, Password)
- There's Many Types Of Databases (MongoDB, MySQL, SQLite)
- SQL Stand For Structured Query Language
- SQLite => Can Run in Memory or in A Single File
- You Can Browse File With https://sqlitebrowser.org/
- Data Inside Database Has Types (Text, Integer, Date)

# 118 - Databases – SQLite Create Database And Connect

- Connect
- Execute
- Close

```
# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Create The Tables and Fields
db.execute(
    "create table if not exists skills (name text, progress integer, user_id integer)")

# Close Database
db.close()
```

# 119 - Databases – SQLite Insert Data Into Database

- `cursor` => All Operation in SQL Done By Cursor Not The Connection Itself
- `commit` => Save All Changes

# 120 - Databases - SQLite Retrieve Data From

- `fetchone` => returns a single record or None if no more rows are available.
- `fetchall` => fetches all the rows of a query result. It returns all the rows
  as a list of tuples. An empty list is returned if there is no record to fetch.
- `fetchmany(size)` =>

# 122 - Databases - SQLite Update And Delete From Database

- Update Data
  -- if `where condition` not exist it will update every record

```
# cr.execute("update users set name = 'Ameer' where user_id = 3")
```

- Delete Data
  -- if `where condition` not exist it will delete all records

```
cr.execute("delete from users where user_id = 4")
```

# 127 - Databases - SQLite Very Important Information

- SQL injection

```
cr.execute("insert into skills values('pascal', '65' , 1)")
```

- To avoid sql injection

```
my_tuple = ('pascal', '65' , 1)
cr.execute("insert into skills values(?,?,?)",my_tuple)
```

# 128 - Advanced Lessons - `__name__` And "`__main__`"

- `if __name__ == "__main__":`
- `__name__` => Built In Variable
- "`__main__`" => Value Of The `__name__` Variable
  Executions Methods
- Directly => Execute the Python File Using the Command Line.
- From Import => Import The Code From File To Another File

- In Some Cases You Want To Know If You Are Using A Module Method As Import
- Or You Use The Original Python File

- In Direct Mode Python Assign A Value `__main__`
- To The Built In Variable `__name__` in The Background

# 129 - Advanced Lessons - Timing Your Code With Timeit

- timeit: - Get Execution Time Of Code By Running 1M Time And Give You Minimal Time
  -- It Used For Performance By Testing All Functionality
- timeit(stmt, setup, timer, number)
- timeit(pass, pass, default, 1.000.000) Default Values

- stmt: Code You Want To Measure The Execution Time
- setup: Setup Done Before The Code Execution (Import Module Or Anything)
- timer: The Timer Value
- number: How Many Execution That Will Run

```
import timeit
```

```
print(dir(timeit))

print(timeit.timeit("'Elzero' * 1000"))
```

```
name = "Elzero"

print(name * 1000)

print(timeit.timeit("name = 'Elzero'; name * 1000"))
```

```
# print(random.randint(0, 50))

print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))

print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))
```

# 130 - Advanced Lessons - Add Logging To Your Code

- Print Out To Console Or File
- Print Logs Of What Happens

- `DEBUG()`
- `INFO()`
- `WARNING()`
- `ERROR()`
- `CRITICAL()`

- name => Logging Module Give It To The Default Logger.

- Basic Config
  -- `level` => Level of Severity
  -- `filename` => File Name and Extension
  -- `mode` => Mode Of The File a => Append
  -- `format` => Format For The Log Message

- getLogger => Return a Logger With the Specified Name

```
import logging

# print(dir(logging))

logging.basicConfig(filename="my_app.log",
                    filemode="a",
                    format="(%(asctime)s) | %(name)s | %(levelname)s => '%(message)s'",
                    datefmt="%d - %B - %Y, %H:%M:%S")

my_logger = logging.getLogger("Elzero")

my_logger.warning("This Is Warning Message")
```

# 131 - Advanced Lessons – Unit Testing With Unittest

- Test Runner
  -- The Module That Run The Unit Testing (unittest, pytest)

- Test Case
  -- Smallest Unit Of Testing
  -- It Use Asserts Methods To Check For Actions And Responses
  -Test Suite
  -- Collection Of Multiple Tests Or Test Cases
  -Test Report
  -- A Full Report Contains The Failure Or Succeed

- unittest
  -- Add Tests Into Classes As Methods
  -- Use a Series of Special Assertion Methods
  -- [Link](https://docs.python.org/3/library/unittest.html)

```
import unittest
```

```
assert 3 * 8 == 24, "Should Be 24"

def test_case_one():

  assert 5 * 10 == 50, "Should Be 50"

def test_case_two():

  assert 5 * 50 == 250, "Should Be 250"

if __name__ == "__main__":

  test_case_one()
  test_case_two()

  print("All Tests Passed")
```

```
class MyTestCase(unittest.TestCase):

  def test_one(self):

    self.assertTrue(100 > 99, "Should Be True")

  def test_two(self):

    self.assertEqual(40 + 60, 100, "Should Be 100")

  def test_three(self):

    self.assertGreater(100, 101, "Should Be True")

if __name__ == "__main__":

  unittest.main()
```

# 132 - Advanced Lessons - Generate Random Serial Numbers

# 133 - Flask – Intro And Your First Page

# 134 - Flask – Create HTML Files

# 135 - Flask – Create And Extends HTML Templates

# 136 - Flask - Jinja Template

# 137 - Flask – Advanced CSS Task Using Jinja

# 138 - Flask – Skills Page Using List Data

# 139 - Flask - Customizing App With Css

# 140 - Flask - Adding The JS Files

# 141 - Web Scraping – Control Browser With Selenium

- Control Browser With Selenium For Automated Testing
- Download File From The Internet
- Subtitle Download And Add On Your Movies [ Many Modules ]
- Get Quotes From Websites
- Get Gold and Currencies Rate
- Get News From Websites

- `pip install selenuim`
- `pip install webdriver-manager`

```
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://elzero.org")

browser.find_element_by_css_selector(".search-field").send_keys("Front-End Developer")

browser.find_element_by_css_selector(".search-submit").click()

browser.find_element_by_css_selector(".all-search-posts .search-post:first-of-type h3 a").click()

browser.implicitly_wait(5)

views_count = browser.find_element_by_css_selector(".z-article-info .z-info:last-of-type span:last-child")

browser.implicitly_wait(5)

print(views_count.get_attribute('innerHTML'))

browser.quit()
```

# 142 - NumPy – Intro

- NumPy Is A Python Third-Party Module To Deal With Arrays & Matrices
- NumPy Stand For Numerical Python
- NumPy Is Open Source
- NumPy Support Dealing With Large Multidimensional Arrays & Matrices
- NumPy Has Many Mathematical Functions To Deal With This Elements

- Why We Use NumPy Array
- Consume Less Memory
- Very Fast Compared To Python List
- Easy To Use
- Support Element Wise Operation
- Elements Are Stored Contiguous

- Python Lists
  -- Homogeneous => Can Contains The Same Type of Objects
  -- Heterogeneous => Can Contains Different Types of Objects.

- The Items in The Array Have to Be Of The Same Type
- You Can Be Sure Whats The Storage Size Needed for The Array
- NumPy Arrays Are Indexed From 0

- NumPy On Github => https://github.com/numpy/numpy

```
import numpy as np
print(np.__version__)
```

# 143 - NumPy – Create Arrays

```
import numpy as np
```

```
# print(dir(np))

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print(my_list)
print(my_array)

print("#" * 50)
```

- Type

```
print(type(my_list))
print(type(my_array))

print("#" * 50)
```

- Accessing Elements

```
print(my_list[0])
print(my_array[0])

print("#" * 50)

a = np.array(10)
b = np.array([10, 20])
c = np.array( [ [1, 2], [3, 4] ] )
d = np.array( [ [ [5, 6], [7, 9] ], [ [1, 3], [4, 8] ] ] )

print(d[1][1][-1])
print(d[1, 1, 1])
print(d[1, 1, -1])

print("#" * 50)
```

- Number Of Dimensions

```
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print("#" * 50)
```

- Custom Dimensions

```
my_custom_array = np.array([1, 2, 3], ndmin=3)
print(my_custom_array)
print(my_custom_array.ndim)

print(my_custom_array[0, 0, 0])
```

# 144 - NumPy – Compare Data Location And Type

```
import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array([1, 2, 3, 4, 5])

print(my_list[0])
print(my_list[1])

print(my_array[0])
print(my_array[1])

print("#" * 50)

print(id(my_list[0]))
print(id(my_list[1]))

print(id(my_array[0]))
print(id(my_array[1]))

print("#" * 50)

my_list_of_data = [1, 2, "A", "B", True, 10.50]
my_array_of_data = np.array([1, 2, "A", "B", True, 10.50])

print(my_list_of_data)
print(my_array_of_data)

print("#" * 50)

print(my_list_of_data[0])
print(my_array_of_data[0])

print(type(my_list_of_data[0]))
print(type(my_array_of_data[0]))

print("#" * 50)

my_list_of_data_two = [1, 2, "A", "B", True, 10.50]
my_array_of_data_two = np.array([1, 2, "A"])

print(my_list_of_data_two)
print(my_array_of_data_two)

print("#" * 50)

print(my_list_of_data_two[0])
print(my_array_of_data_two[0])

print(type(my_list_of_data_two[0]))
print(type(my_array_of_data_two[0]))
```

# 145 - NumPy – Compare Performance And Memory Use

- One line loop
  -- Noraml

````
for n1, n2 in zip(my_list1, my_list2):
    print(n1 + n2)
    ```
````

-- Shorten

```
[(n1 + n2) for n1, n2 in zip(my_list1, my_list2)]
```

- COde

```
import numpy as np
import time
import sys

elements = 150000

my_list1 = range(elements)
my_list2 = range(elements)

my_array1 = np.arange(elements)
my_array2 = np.arange(elements)

list_start = time.time()
list_result = [(n1 + n2) for n1, n2 in zip(my_list1, my_list2)]
print(f"List Time: {time.time() - list_start}")

array_start = time.time()
array_result = my_array1 + my_array2
print(f"Array Time: {time.time() - array_start}")

# for n1, n2 in zip(my_list1, my_list2):

# 	print(n1 + n2)

print(list_result)
print(array_result)

my_array = np.arange(100)

print(my_array)
print(my_array.itemsize)
print(my_array.size)
print(f"All Bytes: {my_array.itemsize * my_array.size}")

print("#" * 50)

my_list = range(100)
print(sys.getsizeof(1))
print(len(my_list))
print(f"All Bytes: {sys.getsizeof(1) * len(my_list)}")
```

# 146 - NumPy – Array Slicing

- Slicing => [Start:End:Steps] Not Including End

```
import numpy as np

# Slicing => [Start:End:Steps] Not Including End

a = np.array(["A", "B", "C", "D", "E", "F"])

print(a.ndim)
print(a[1])
print(a[1:4])
print(a[:4])
print(a[2:])

print("#" * 50)

b = np.array([["A", "B", "X"], ["C", "D", "Y"], ["E", "F", "Z"], ["M", "N", "O"]])

print(b.ndim)
print(b[1])

print("#" * 50)

print(b[2:, :2])
print(b[2:, :2:2])
```

# 147 - NumPy – Data Types And Control Array

- [Data types](https://numpy.org/devdocs/user/basics.types.html)
- [Specifying and constructing data types](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types)

- `?` boolean
- `b` (signed) byte
- `B` unsigned byte
- `i` (signed) integer
- `u` unsigned integer
- `f` floating-point
- `c` complex-floating point
- `m` timedelta
- `M` datetime
- `O` (Python) objects
- `S`, 'a' zero-terminated bytes (not recommended)
- `U` Unicode string
- `V` raw data (void)

```
import numpy as np
```

- Show Array Data Type

```
my_array1 = np.array([1, 2, 3])
my_array2 = np.array([1.5, 20.15, 3.601])
my_array3 = np.array(["Osama_Elzero", "B", "Ahmed"])

print(my_array1.dtype)
print(my_array2.dtype)
print(my_array3.dtype)

print("#" * 50)
```

- Create Array With Specific Data Type

```
my_array4 = np.array([1, 2, 3], dtype=float) # float Or 'float' Or 'f'
my_array5 = np.array([1.5, 20.15, 3.601], dtype=int) # int Or 'int' Or 'i'
# my_array6 = np.array(["Osama_Elzero", "B", "Ahmed"], dtype=int) # Value Error

print(my_array4.dtype)
print(my_array5.dtype)
# print(my_array6.dtype)

print("#" * 50)
```

- Change Data Type Of Existing Array

```
my_array7 = np.array([0, 1, 2, 3, 0, 4])
print(my_array7.dtype)
print(my_array7)

print("#" * 50)

my_array7 = my_array7.astype('float')
print(my_array7.dtype)
print(my_array7)

print("#" * 50)

my_array7 = my_array7.astype('bool')
print(my_array7.dtype)
print(my_array7)

print("#" * 50)
```

- Test Capacity

```
my_array8 = np.array([100, 200, 300, 400], dtype='f')
print(my_array8.dtype)
print(my_array8[0].itemsize) # 4 Bytes

my_array8 = my_array8.astype('float') # Change To Float64
print(my_array8.dtype)
print(my_array8[0].itemsize) # 8 Bytes
```

# 148 - NumPy – Arithmetic And Useful Operations

- `min`
- `max`
- `sum`
- `ravel` => Returns Flattened Array 1 Dimension With Same Type

```
import numpy as np
```

- Arithmetic Operations

```
my_array1 = np.array([10, 20, 30])
my_array2 = np.array([5, 2, 4])

print(my_array1 + my_array2) # result [15, 22, 34]
print(my_array1 - my_array2) # result [5, 18, 26]
print(my_array1 * my_array2) # result [50, 40, 120]
print(my_array1 / my_array2) # result [2, 10, 7.5]

print('#' * 50)

my_array3 = np.array([[1, 4], [5, 9]])
my_array4 = np.array([[2, 7], [10, 5]])

print(my_array3 + my_array4) # result [ [3, 11], [15, 14] ]
print(my_array3 - my_array4) # result [ [-1, -3], [-5, 4] ]
print(my_array3 * my_array4) # result [ [2, 28], [50, 45] ]
print(my_array3 / my_array4) # result [ [0.5, 0.57142857], [0.5, 1.8] ]

print('#' * 50)
```

- Min, Max, Sum

```
my_array5 = np.array([10, 20, 30])
print(my_array5.min())
print(my_array5.max())
print(my_array5.sum())

print('#' * 50)

my_array6 = np.array([[6, 4], [3, 9]])
print(my_array6.min())
print(my_array6.max())
print(my_array6.sum())

print('#' * 50)
```

- Ravel

```
my_array7 = np.array([[6, 4], [3, 9]])
print(my_array7.ravel())

my_array8 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(my_array8.ndim)
print(my_array8.ravel())
x = my_array8.ravel()
print(x.ndim)
```

# 149 - Numpy - Array Shape And ReShape

- Shape Returns A Tuple Contains The Number Of Elements in Each Dimension

```
import numpy as np
```

```
my_array1 = np.array([1, 2, 3, 4])
print(my_array1.ndim)
print(my_array1.shape)

print("#" * 50)

my_array2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print(my_array2.ndim)
print(my_array2.shape)

print("#" * 50)

my_array3 = np.array([[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]])
print(my_array3.ndim)
print(my_array3.shape)

print("#" * 50)

my_array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(my_array4.ndim)
print(my_array4.shape)

reshaped_array4 = my_array4.reshape(3, 4)
print(reshaped_array4.ndim)
print(reshaped_array4.shape)
print(reshaped_array4)

print("#" * 50)

my_array5 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print(my_array5.ndim)
print(my_array5.shape)

print("#" * 50)

# reshaped_array5 = my_array5.reshape(-1)
# reshaped_array5 = my_array5.reshape(4, 5)
reshaped_array5 = my_array5.reshape(2, 5, 2)
print(reshaped_array5.ndim)
print(reshaped_array5.shape)
print(reshaped_array5)
```

# 150 - Virtual Environment Part 1

- Virtual Environment exsist to handle packages

- Create `env` folder
- open folder in terminal
- Run=> `python -m venv envNamw`
  -- `python -m venv ai`

- U can have multi environment
  -- `python -m venv ai`
  -- `python -m venv fire`

# 151 - Virtual Environment Part 2

- To activate certin environment => `source envName/Scripts/activate`
  -- `source ai/Scripts/activate`
- `deactivate` => To close environment

- `which python` => To show where python run from

- To run file from env `envName/Scripts/python.exe {path of file u want to run}`
  -- `ai/Scripts/python.exe d:/python/151/main.py`

- `pip freeze` => To output all packages and its version from current environment
  -- to make a file from this command u can use unix commands lik `command > fileName`
  -- `pip freeze > requirements.txt`

- `pip install -r FILE` => To install packages from file
  -- `pip install -r requirements.txt`

- Virtual Environment Wrapper?

# 152 - The End And Resources

- [Resources](https://www.youtube.com/watch?v=OwV5R8Qy1e4&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs&index=152)
  -- [awesome-python](https://awesome-python.com/)

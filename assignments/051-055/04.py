students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

letter_equivlent = {
  "A":100,
  "B":80,
  "C":40,
  "D":20
}

table_width = 40
for student,subjects in students.items():
  # print Header
  print('"'+"-"*table_width +'"')
  print('"'+(f"Student Name => {student}").center(table_width)+'"')
  print('"'+"-"*table_width +'"')

  total = 0
  # loop for subjects
  for subject,degree in subjects.items():
    print('"'+(f"- {subject} => {letter_equivlent[degree]} Points").center(table_width)+'"')
    total += letter_equivlent[degree]
  else:
    print('"'+f"Total Points For {student} Is {total}".center(table_width)+'"')

# print(len("------------------------------"))

# Needed Output
# "------------------------------"
# "-- Student Name => Ahmed"
# "------------------------------"
# "- Math => 100 Points"
# "- Science => 20 Points"
# "- Draw => 80 Points"
# "- Sports => 40 Points"
# "- Thinking => 100 Points"
# "Total Points For Ahmed Is 340"
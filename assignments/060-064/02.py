def get_people_scores(name="",**subjects):
  print("-"*40)
  if (name and not subjects):
    print(f"Hello {name} You Have No Scores To Show")
  elif(name and subjects):
    print(f"Hello {name} This Is Your Score Table:")
    for key,value in subjects.items():
      print(f"{key} => {value}")
  else:
    for key,value in subjects.items():
      print(f"{key} => {value}")
    
  print("-"*40)

# Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"

# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)

# Output
"Hello Mahmoud This Is Your Score Table:"
"Logic => 70"
"Problems => 60"

# Test 3
get_people_scores(Logic=70, Problems=60)

# Output
"Logic => 70"
"Problems => 60"

# Test 4
get_people_scores("Ahmed")

# Output
"Hello Ahmed You Have No Scores To Show"
def get_the_scores(name="",**subjects):
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

scores_list = {
  "Math" : 90,
  "Science" : 80,
  "Language" : 70
}

# Test 1
get_the_scores("Osama", **scores_list)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"

# Test 2
get_the_scores("Osama")

# Output
"Hello Osama You Have No Scores To Show"

# Test 3
get_the_scores(**scores_list)

# Output
"Math => 90"
"Science => 80"
"Language => 70"
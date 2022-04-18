# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

letter_equvilent = {
  "A" : 100,
  "B" : 80,
  "C" : 40,
}

# Needed Output
"My Rank in Math Is A And This Equal 100 Points"
"My Rank in Science Is B And This Equal 80 Points"
"My Rank in Drawing Is A And This Equal 100 Points"
"My Rank in Sports Is C And This Equal 40 Points"
"Total Points Is 320"

total = 0

for skil,degree in my_ranks.items():
  print(f"My Rank in {skil} Is {degree} And This Equal {letter_equvilent[degree]} Points")
  total += letter_equvilent[degree]
else:
  print(f"Total Points Is {total}")
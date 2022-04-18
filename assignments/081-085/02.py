def hashMaker(fun):
  def maker():
    print("Sugar Added From Decorators")
    fun()
    print("####################")
  return maker

# Create Your Decorator Here

@hashMaker
def make_tea():
  print("Tea Created")

@hashMaker
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()

# Needed Output

"Sugar Added From Decorators"
"Tea Created"
"####################"
"Sugar Added From Decorators"
"Coffe Created"
"####################"
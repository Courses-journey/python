def framedMsg(msg,width=40):
  return f'{"-"*width}\n|{msg.center(width-2)}|\n{"-"*width}'

def say_hello(name="Unknown", age = "Unknown", country="Unknown"):
  return f"Hello {name} Your Age Is {age} And You Live In {country}"


print(say_hello("Osama", 38, "Egypt"))
print(say_hello())
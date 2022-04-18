def show_skills(name,*skils):
  print( framedMsg(f"Hello {name} Your Skills are"))
  if len(skils) == 0:
    print( framedMsg(f"Hello {name} You Have No Skills To Show"))
  else:
    for skil in skils:
      print( framedMsg(skil))


def framedMsg(msg,width=40):
  return f'{"-"*width}\n|{msg.center(width-2)}|\n{"-"*width}'

# Input
show_skills("Osama", "HTML", "CSS", "JS", "Python")

show_skills("Ahmed")
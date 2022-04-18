def calculate(num1,num2,operation = "add"):
  if str(operation).lower() == "add" or operation.lower()== "a":
    # return num1 + num2
    return framedMsgs(f"Add | {num1} + {num2} = {num1 + num2}")
  elif operation.lower() == "multiply" or operation.lower() == "m":
    # return num1 * num2
    return framedMsgs(f"Multiply | {num1} x {num2} = {num1 * num2}")
  elif operation.lower() == "subtract" or operation.lower() == "s":
    # return num1 - num2
    return framedMsgs(f"Subtract | {num1} - {num2} = {num1 - num2}")
  else :
    return framedMsgs("Use [add | multiply | subtract]")

def framedMsgs(msg,width=40):
  return f'{"-"*width}\n|{msg.center(width-2)}|\n{"-"*width}'

print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200

print(calculate(10, 20, "h")) # 200
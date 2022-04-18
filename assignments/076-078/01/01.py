import random

"Random Number Between 10 And 50 =>" "Show The Random Number Here"
"Random Even Number Between 2 And 10 =>" "Show The Random Even Number Here"
"Random Odd Number Between 1 And 9 =>" "Show The Random Odd Number Here"

# Module Methods Content Here

print(f"Random Number Between 10 And 50 => {random.randint(10,50)}")
print(f"Random Number Between 2 And 10 => {random.randint(2,10)}")
print(f"Random Number Between 1 And 9 => {random.randint(1,9)}")

print(dir(random))
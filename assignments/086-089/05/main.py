"""
Assignment solution
"""

my_friends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> list:
    ''' Function to say Hello'''
    for someone in some_peoples:
        print(f"Hello {someone}")

say_hello(my_friends)

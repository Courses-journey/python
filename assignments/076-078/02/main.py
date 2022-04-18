import os
import sys

dirName =os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{dirName}\Python\\")

import my_mod
my_mod.say_welcome("Osama")
my_mod.say_hello("Osama")

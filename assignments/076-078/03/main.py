import os
import sys

dirName =os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{dirName}\Python\\")

from my_mod import say_welcome

say_welcome("Osama")

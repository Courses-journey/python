"""
DOC
"""

LETTER = input("Add Letter From A to Z")

try:
    if not LETTER.isalpha() or LETTER.upper() != LETTER:
        raise ValueError
    if len(LETTER) > 1:
        raise IndexError
    print(f"You Typed {LETTER}")
except IndexError:
    print("You Must Write One Character Only")
except ValueError:
    print("The Letter Not In A - Z")

"""
DOC
"""

try:
    number = input("Add Your Number ")
    if str(number).isalpha():
        raise Exception("Only Numbers Allowed")
    else:
        number = int(number)
    if len(str(number)) > 1:
        raise IndexError("Only One Character Allowed")
    if number>0:
        print("####################")
        print(f"The Number Is {number}")
        print("####################")
    else:
        raise ValueError("Number Must Be Larger Than 0")
finally:
    pass

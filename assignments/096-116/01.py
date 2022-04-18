"""
DOC
"""

class Game:
    '''Doc'''
    def __init__(self,name,developer,year,price):
        '''Doc'''
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price
    def price_in_pounds(self):
        '''Doc'''
        return f"Price In Egypt Is {self.price * 18.43} Egyptian Pounds"


game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

# Needed Output
# "Game Name Is "Ys", Developer Is "Falcom",
# Release Date Is "2010",
# Price In Egypt Is 780.0 Egyptian Pounds"

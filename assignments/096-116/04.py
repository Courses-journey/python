"""
DOC
"""


# from typing import overload


class Games:
    '''Doc'''
    # @overload
    # def __init__(self,game_name:str):
    #     '''DOC'''
    #     self.game = game_name

    # @overload
    # def __init__(self,game_list:list):
    #     '''DOC'''
    #     self.game = game_list

    # def __init__(self,games_count:float):
    #     '''DOC'''
    #     self.game = games_count

    def __init__(self,game):
        '''DOC'''
        self.game = game

    def show_games(self):
        '''DOC'''
        if isinstance(self.game,str):
            print(f'I Have One Game Called "{self.game}"')

        elif isinstance(self.game,list):
            print('I Have Many Games:')
            for item  in self.game:
                print(f"-- {item}")

        elif isinstance(self.game,int) or isinstance(self.game,float) :
            print(f"I Have {self.game} Game.")

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.

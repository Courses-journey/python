"""
DOC
"""

class User:
    '''Doc'''
    def __init__(self,name,middle_name,age,gender):
        '''Doc'''
        self.name = name
        self.middle_name = middle_name
        self.age = age
        self.gender = gender
    def full_details(self):
        '''Doc'''
        return f'Hello Mr {self.name} {self.middle_name[0]}. [{40-self.age}] Years To Reach 40'

user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40

"""
DOC
"""

class Members:
    '''DOC'''
    def __init__(self, n, p):
        '''DOC'''
        self.name = n
        self.permission = p

    def show_info(self):
        '''DOC'''
        return f"Your Name Is {self.name} And You Are {self.permission}"

# Create Admin Class Here
class Admins(Members):
    '''DOC'''
# Create Moderators Class Here
class Moderators(Members):
    '''DOC'''

member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator

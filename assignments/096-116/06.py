"""
DOC
"""

class A:
    '''DOC'''
    def __init__(self, one):
        '''DOC'''
        self.one = one

class B:
    '''DOC'''
    def __init__(self, two):
        '''DOC'''
        self.two = two

class C:
    '''DOC'''
    def __init__(self, three):
        '''DOC'''
        self.three = three

# Write The Class Called "Text" Here
class Text(A,B,C):
    '''DOC'''
    def __init__(self, one,two,three):
        '''DOC'''
        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)
    def show_name(self):
        '''DOC'''
        return f"The Name Is {self.one}{self.two}{self.three}"

the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero

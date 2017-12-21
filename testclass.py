class MyClass:
    """A simple example class """
    i = 12345

    def __init__(self):
        self.data = []

    def getdata(self):
        return self.data

    def f(self):
        return 'hello world'

class Dog:
  
    def __init__(self, name):
        self.name = name
        self.tricks = []  

    def add_trick(self, trick):
        self.tricks.append(trick)

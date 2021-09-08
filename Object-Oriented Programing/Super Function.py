class Parent:
    def __init__(self):
        print('Parent')
    def name(self,name):
        self.name=name
        print(self.name)

class Child(Parent):
    def __init__(self):
        print('Child')
        super().__init__() #Super Function allows us to call init function from the other class
        Parent().name('Mubashir')

child=Child()

print(Child.__mro__) #Method Resolution Order provides us the order of all the classes,Functions and objects which are to be executed.


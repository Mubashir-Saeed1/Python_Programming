from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.__side=side

    def area(self):
        return self.__side**2

    def perimeter(self):
        return 4*self.__side

    def display(self):
        pass
    
#Now we are not able to create instants of Parent as well as Child class until we don't implement all the methods of Parent class to Child class.
#shape=Shape()
square=Square(4)
square.display()

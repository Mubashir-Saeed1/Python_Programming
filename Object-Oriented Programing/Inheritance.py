class Polygon:
    def __init__(self):
        self.__width=None
        self.__height=None
        
    def set_values(self,width,height):
        self.__width=width
        self.__height=height
        
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
class Rectangle(Polygon):
    def area(self):
        return self.get_width()*self.get_height()
    
class Triangle(Rectangle):
    def area(self):
        return self.get_width()*self.get_height()/2

rectangle=Rectangle()
triangle=Triangle()
rectangle.set_values(40,50)
triangle.set_values(40,50)
rarea=rectangle.area()
tarea=triangle.area()
print(f'Area of Rectangle = {rarea}')
print(f'Area of Triangle = {tarea}')

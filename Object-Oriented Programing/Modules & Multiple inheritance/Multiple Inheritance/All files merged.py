class Polygon:
    __width=0
    __height=0

    def set_values(self,width,height):
        self.__width=width
        self.__height=height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height
class Shape:
    __color=None

    def set_color(self,color):
        self.__color=color

    def get_color(self):
        return self.__color
    
class Rectangle(Polygon,Shape):
    def area(self):
        area=self.get_width()*self.get_height()
        print(f'Area of Rectangle = {area}')
        print(f'Color of Rectangle = {self.get_color()}')

class Triangle(Polygon,Shape):
    def area(self):
        area=self.get_width()*self.get_height()/2
        print(f'Area of Triangle = {area}')
        print(f'Color of Triangle = {self.get_color()}')

Rect=Rectangle()
Tri=Triangle()

Rect.set_values(40,50)
Tri.set_values(40,50)

Rect.set_color('Green')
Tri.set_color('Red')

Tri.area()
Rect.area()

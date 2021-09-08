from Polygon import Polygon
from Shape import Shape

class Rectangle(Polygon,Shape):
    def area(self):
        area=self.get_width()*self.get_height()
        print(f'Area of Rectangle = {area}')
        print(f'Color of Rectangle = {self.get_color()}')

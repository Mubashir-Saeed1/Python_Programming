from Polygon import Polygon
from Shape import Shape

class Triangle(Polygon,Shape):
    def area(self):
        area=self.get_width()*self.get_height()/2
        print(f'Area of Triangle = {area}')
        print(f'Color of Triangle = {self.get_color()}')
    

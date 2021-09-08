class car:
    def __init__(self,speed,color):
        self.__speed=speed #To declare members privately(they cannot be used outsite the class).
        self.__color=color
        
    def set_speed(self,value):
        self.__speed=value

    def get_speed(self):
        return self.__speed

    def set_color(self,value):
        self.__color=value

    def get_color(self):
        return self.__color

    def __private(self):  #To declare method privately.It also cannot be used outside the class.
        print('This is a Private Method')

    def display(self):
        print(f'Speed = {self.__speed}')
        print(f'Color = {self.__color}')
        self.__private()

ford=car(200,'Black')
honda=car(300,'White')
audi=car(400,'Red')

print('For Ford')
ford.display()
print('For Honda')
honda.display()
print('For Audi')
audi.display()

ford.set_speed(300)
ford.set_color('Yellow')
honda.set_speed(400)
honda.set_color('Green')
audi.set_speed(500)
audi.set_color('Blue')

print('Updated')
print('For Ford')
ford.display()
print('For Honda')
honda.display()
print('For Audi')
audi.display()
ford.__private() #This will give an error.

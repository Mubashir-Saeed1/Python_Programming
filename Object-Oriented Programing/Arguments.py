class First:
    def __init__(self,*kwargs):
        print('My First Program')
        self.age=19
        a=kwargs
        print(a,self.age)

name='Saima Mubashir'
a=2
c=3
first=First(name,a,c)
second=First()

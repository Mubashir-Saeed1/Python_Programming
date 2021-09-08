#Overloading == with our own value

class A:
    def __init__(self,a):
        self.a=a

    def __eq__(self,other):
        return self.a==2

a=A(4)
b=A(2)

if b==a:
    print('Yes')
else:
    print('No')

#Overloading - with *
    
class B:
    def __init__(self,a):
        self.a=a

    def __sub__(self,value):
        return (self.a * value.a)

num1=B(int(input('Enter Number 1 = ')))
num2=B(int(input('Enter Number 2 = ')))

print(num1-num2)

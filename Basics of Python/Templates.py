from string import Template
from array import array
t=Template('x is $x')
print(t.substitute({'x':1}))

Student=[('Mubashir',90),('Hassan',87),('Zeeshan',56),('Jamshid',67)]

tem=Template('Hi $name, You have got $marks Marks')

for x in Student:
    print(tem.substitute(name=x[0],marks=x[1]))

lis=[3,4,6,2,7,4]
print(lis)
ar=array('i',lis)
print(ar)

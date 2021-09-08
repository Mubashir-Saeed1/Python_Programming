a=50
b=100
if b>a:
    print("Yes")
c=50
d=50
if c>d:
    print('c is greater')
elif d>c:
    print('d is greater')
else:
    print('Both are equal')
a=40
b=45
if a>b:
    print('a is greater')
else:
    print('b is greater')
a,b=40,40
if a==b: print('both a,b are equal')
print('a is greater') if a>b else print ('b is greater') if b>a else print('both a&b are equal')
a,b,c=4,6,9
if c>b and c>a:
    print('c is greatest')
if b>a or b>c:
    print('b is greater than one of the given numbers')

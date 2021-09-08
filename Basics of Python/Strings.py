email='''
Hi john,

This is our First email to you.

Thank You,
The Support Team.
'''
print(email)
print('******************************Starting New Line*********************************')
course='python for beginners'
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[1:])
print(course[:5])
print(course[:])
another=course[::-1]
print(another)
print('******************************Starting New Line*********************************')
print('Formatted Sting')
first='Mubashir'
last='Saeed'
message=f'{first} {last} is a Coder'
print(message)
print('******************************Starting New Line*********************************')
print('python' in course)
for x in range(0,len(course)):
    print(course[x])
print(course.title())
print(course.find('t'))

i=0
while i<=6:
    print(i)
    i+=1
print("Start New Line")
i=0
while i<=6:
    print(i)
    if i==3:
        break
    i+=1
print("Start New Line")
i=0
while i<=6:
    i+=1
    if i==3:
        continue
    print(i)
else:
    print('Done')#Else will be executed if the while loop completes successfully
print("Start New Line")
fruits=['apple','banana','cherry','mango','orange']
for x in fruits:
    print(x)
print("Start New Line")
for x in fruits:
    print(x)
    if x=='banana':
        break
print("Start New Line")
for x in fruits:
    if x=='banana':
        continue
    print(x)
print("Start New Line")
for x in range(6):
    print(x)
print("Start New Line")
for x in range(2,6):
    print(x)
print("Start New Line")
for x in range(0,30,3):
    print(x)
print("Start New Line")
for x in range(0,40,4):
    print(x)
else:
    print('Loop Finished')
print("Start New Line")
adj=['red','juicy','tasty']
fruit=['apple','mango','banana','cherry']
for x in adj:
    for y in fruit:
        print(x,y)

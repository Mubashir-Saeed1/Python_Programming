list=['mango','ornagel','banana'] #declaring list
print(list)
l='i am a boy'#declaring a string
print(l)
print(l.upper()) #convert to uppercase letters
print(l.lower())    #convert to lowercase letters
print(l.split("a")) #split sentence from given letter
print (list[1])
list[1]="apple" #add apple to the index 1 in list
print(list)
for x in list: #print list using for loop
    print(x)
if 'mango' in list: #check if mango is available in the list
    print("Yes")
if 'cherry' in list: #check if cherry is available in the list
    print("cheery in the list")
k=len(list) #printing length of the list
print(k)
for x in range(5): #syntax of for loop
    print(" ")
    for y in range(x):
        print('*')
list.append("giant") #adding giant to the end of the list
print (list)
list.remove('banana') #removing banana from the list
print(list)
list.insert(3,'melon') #inserting melon at index 3 to the list
print(list)
list.pop() #removing last element of the list
print(list)
del list [2] #deleting element from index 2 from the list
print(list)
list.clear()#clearing the list
print(list)
a=int(6)
b=int(20)
sum=a+b
print(sum)
exp=a**b #exponential function
print(exp)
print(1+3)
a=int(10)
b=int(3)
if a>b:
    print('yes')
fd=a//b #floor division(print quotient excluding digits after decimal point)
print(fd)

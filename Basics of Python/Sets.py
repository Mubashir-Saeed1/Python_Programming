sets={'apple','banana','cherry','mango'}
print(sets)
for x in sets:
    print(x)
if 'cherry' in sets:
    print('Yes')
sets.add("orange")
print(sets)
sets.update(['chilli','potato','alpha'])
print(sets)
l=int(len(sets))
print(l)
sets.remove('alpha')
print(sets)
sets.discard('potato')
print(sets)
sets.clear()
print(sets)
del sets     #if an error appears in a line in the middle of the code then the remaining lines will not be executed in python
seta={'apple','mango','banana','cherry'}
setb={'apple','mango','banana','cherry','orange'}
print(seta)
print(setb)

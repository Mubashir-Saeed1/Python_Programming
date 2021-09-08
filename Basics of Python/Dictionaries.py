dic={
    'brand':'ford',
    'model':'mustang',
    'year':1964
    }
print(dic)
x=dic.get('model')
print(x)
x=dic['brand']
print(x)
dic['year']=2018
print(dic)
for x in dic:
    print (x)
for x in dic:
    print(dic[x])
print(dic['year'])
for x,y in dic.items():
    print(x,y)
if 'model'in dic:
    print('yes')
x=len(dic)
print(x)
dic['color']='white'
print(dic)
for x,y in dic.items():
    print(x,y)
dic.popitem()
print(dic)
dic.pop('model')
print(dic)
del dic['year']
print(dic)
del dic
#dic.clear() clears all the values in the dictionary
dic1={
    'brand':'ford',
    'model':'mustang',
    'year':1964
    }
print(dic1.keys())
print(dic1['model'])

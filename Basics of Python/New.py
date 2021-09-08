
>>> a='hellow world'
>>> print (a)
hellow world
>>> print (a.split(","))
['hellow world']
>>> b='i am a boy'
>>> b.split("m")
['i a', ' a boy']
>>> a.split('o')
['hell', 'w w', 'rld']
>>> list=["apple', 'banana', 'cherry', 'monkey']
      
SyntaxError: EOL while scanning string literal
>>> list=["apple", 'banana', 'cherry', 'monkey']
>>> print (list)
['apple', 'banana', 'cherry', 'monkey']
>>> print (list[0])
apple
>>> list[2]="mango"
>>> print (list)
['apple', 'banana', 'mango', 'monkey']
>>> list[3]="cherry"
>>> print (list)
['apple', 'banana', 'mango', 'cherry']
>>> for x in list
SyntaxError: invalid syntax
>>> for x in list:
	>>>print(x)
	
SyntaxError: invalid syntax
>>> for x in list;
SyntaxError: invalid syntax
>>> for x in list:
	print(x)

	
apple
banana
mango
cherry
>>> if 'cherry' in list:
	print('Ys')

	
Ys
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> l=len(list)
>>> print(l)
4
>>> list.append(orange)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    list.append(orange)
NameError: name 'orange' is not defined
>>> list.append('orange')
>>> print (list)
['apple', 'banana', 'mango', 'cherry', 'orange']
>>> list.insert[3]('guava')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list.insert[3]('guava')
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> list.insert(3,'guava')
>>> print (list)
['apple', 'banana', 'mango', 'guava', 'cherry', 'orange']
>>> list.remove('banana')
>>> print(list)
['apple', 'mango', 'guava', 'cherry', 'orange']
>>> list.remove([2])
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    list.remove([2])
ValueError: list.remove(x): x not in list
>>> list.insert(1, "banana")
>>> print(list)
['apple', 'banana', 'mango', 'guava', 'cherry', 'orange']
>>> list.pop()
'orange'
>>> print(list)
['apple', 'banana', 'mango', 'guava', 'cherry']
>>> del list[2]
>>> print(list)
['apple', 'banana', 'guava', 'cherry']
>>> del list()
SyntaxError: can't delete function call
>>> del list
>>> print (list)
<class 'list'>
>>> print(list)
<class 'list'>
>>> list=['Mango','orange', 'banana']
>>> print(list)
['Mango', 'orange', 'banana']
>>> clear list()
SyntaxError: invalid syntax
>>> list.clear
<built-in method clear of list object at 0x00000000006FA808>
>>> print (list)
['Mango', 'orange', 'banana']
>>> list.clear
<built-in method clear of list object at 0x00000000006FA808>
>>> 
>>> print(list)
['Mango', 'orange', 'banana']
>>> list.clear()
>>> print(list)
[]
>>> stuple=('mangp','orange','banana')
>>> print(stuple)
('mangp', 'orange', 'banana')
>>> stuple[1]="alpa"
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    stuple[1]="alpa"
TypeError: 'tuple' object does not support item assignment
>>> list =["applww",'banana','mango']
          print (list)
          
          

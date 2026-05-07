Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='raja'
#s.replace(old,new)
s.replace('a','f')
'rfjf'

= RESTART: C:/Users/ANAND/AppData/Local/Programs/Python/Python312/functions on string.py

= RESTART: C:/Users/ANAND/AppData/Local/Programs/Python/Python312/functions on string.py

= RESTART: C:/Users/ANAND/AppData/Local/Programs/Python/Python312/functions on string.py
s
'raja'
s.find('a)
       
SyntaxError: unterminated string literal (detected at line 1)
s.find('a')
       
1

l=[10,20,30,40]
l.max()
       
SyntaxError: multiple statements found while compiling a single statement
l=[10,20,30]
       
l.max()
       
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    l.max()
AttributeError: 'list' object has no attribute 'max'
l.max(l)
       
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    l.max(l)
AttributeError: 'list' object has no attribute 'max'
l.Max(l)
       
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    l.Max(l)
AttributeError: 'list' object has no attribute 'Max'
min(l)
       
10
max(l)
       
30
sum(l)
       
60
avg(l)
       
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    avg(l)
NameError: name 'avg' is not defined
sum(l)
       
60
sorted(l)
       
[10, 20, 30]
l=[12,1,13]
       
l
       
[12, 1, 13]
sorted(l)
       
[1, 12, 13]
s={10,20,30,40}
       
s.discard(100)
       
s
       
{40, 10, 20, 30}
s.remove(100)
       
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s.remove(100)
KeyError: 100
s
       
{40, 10, 20, 30}
s1={10,20,30}
       
s1
       
{10, 20, 30}
s2={30,40,50}
       
s2
       
{40, 50, 30}
s1.union(s2)
       
{50, 20, 40, 10, 30}
s1.intersection(s2)
       
{30}
s1.difference(s2)
       
{10, 20}
s1.update(23)
       
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s1.update(23)
TypeError: 'int' object is not iterable
s1
       
{10, 20, 30}
s2
       
{40, 50, 30}
s1.difference_update(s2)
       
s1
       
{10, 20}
s2
       
{40, 50, 30}
s1.update({10})
       
s1
       
{10, 20}
s1.update({30})
       
s1
       
{10, 20, 30}
s1.symmetric_difference(s2)
       
{40, 10, 50, 20}
s1
       
{10, 20, 30}
s2
       
{40, 50, 30}
s1.symmetric_difference_update(s2)
       
s1
       
{40, 10, 50, 20}
s2
       
{40, 50, 30}
s1.discard({40})
       
s1
       
{40, 10, 50, 20}
s2
       
{40, 50, 30}
s1
       
{40, 10, 50, 20}
s1.remove({40,50})
       
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s1.remove({40,50})
KeyError: {40, 50}
s1.remove({40})
       
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s1.remove({40})
KeyError: {40}
s1.isdisjoint()
       
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s1.isdisjoint()
TypeError: set.isdisjoint() takes exactly one argument (0 given)
s1.isdisjoint(10)
       
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s1.isdisjoint(10)
TypeError: 'int' object is not iterable
s1.isdisjoint(s2)
       
False
s1.issubset(s2)
       
False
# life is so tragedic
       

'
       
SyntaxError: unterminated string literal (detected at line 1)
''
       
''
str
       
<class 'str'>
cls
       
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
clear
       
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
str('s1')
       
's1'
dir(dict)
       
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""
       
"\n'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'\n"
d
       
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
dic={'a':2,'b':1}
       
dic
       
{'a': 2, 'b': 1}
dic.copy()
       
{'a': 2, 'b': 1}
dic1=dic.copy()
       
dic1
       
{'a': 2, 'b': 1}
dic
       
{'a': 2, 'b': 1}
dic.get('a')
       
2
dic.items()
       
dict_items([('a', 2), ('b', 1)])
dic.keys()
       
dict_keys(['a', 'b'])
dic.fromkeys('a')
       
{'a': None}
dic.values()
       
dict_values([2, 1])
dic.update(['a',3])
       
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    dic.update(['a',3])
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dic.pop('a')
       
2
dic
       
{'b': 1}
dic.popitem()
       
('b', 1)
dic
       
{}
dic.values()
       
dict_values([])
dic
       
{}
dic.add(
    )
       
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    dic.add(
AttributeError: 'dict' object has no attribute 'add'
dic.update({'a':2,'b':3})
dic
{'a': 2, 'b': 3}
dic.update({'a':13})
dic
{'a': 13, 'b': 3}
# keys are unique know
dic.fromkeys({'a'})
{'a': None}
s['d']='semester_Exam'
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    s['d']='semester_Exam'
TypeError: 'set' object does not support item assignment
l=['a','b','c']
d={}
d.fromkeys(l,'student')
{'a': 'student', 'b': 'student', 'c': 'student'}
d.setdefault('a','anand')
'anand'
d
{'a': 'anand'}
d={'a':10,'b':30}
d
{'a': 10, 'b': 30}
d.setdefault('c')
d
{'a': 10, 'b': 30, 'c': None}
d.setdefault('d',40)
40
d
{'a': 10, 'b': 30, 'c': None, 'd': 40}
dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

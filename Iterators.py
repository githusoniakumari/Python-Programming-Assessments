# #------------------------------------------ITERATORS-----------------------------------------#
# This is done in IDLE Shell.
# Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# l=[10,20,30,40]
# id(l[1])
# 140709224451096
# id(l[2])
# 140709224451416
# i=iter(l)
# print(next(i))
# 10
# print(next(i))
# 20
# print(next(i))
# 30
# print(next(i))
# 40
# print(next(i))
# Traceback (most recent call last):
#   File "<pyshell#8>", line 1, in <module>
#     print(next(i))
# StopIteration
# iter(i)
# <list_iterator object at 0x00000122BA4B5270>
# iter(L)
# Traceback (most recent call last):
#   File "<pyshell#10>", line 1, in <module>
#     iter(L)
# NameError: name 'L' is not defined. Did you mean: 'l'?
# iter(l)
# <list_iterator object at 0x00000122BCC03B20>
# iter(i)
# <list_iterator object at 0x00000122BA4B5270>
# id(l)
# 1248707051136
# id(i)
#  1248666014320

# L=[10,20,30]
# print(iter(L))
# <list_iterator object at 0x000001F59DC79BA0>
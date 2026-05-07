""" LAMBDA FUNCTION """
#1
var=lambda coll:coll[::-1] if type(coll) in [list,tuple,str] else False
print(var('Str'))
print(var(2))

#2.
result=lambda substr,string: string.find(substr) if substr in string else substr
print(result('A','Anand'))




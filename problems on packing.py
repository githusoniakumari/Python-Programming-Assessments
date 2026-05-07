#simple programs over packing

# WAP to extract all the int data items present inside the given tuple using packing.

"""
def fname(*a):
    l=[]
    for i in a:
        if type(i)==int:
            l.append(i)
    print(l)
fname(1,'anand',2,4,'uzma',6,9,'sharma','ayantika','manish')
"""
# WAP to extract all the str data items present inside the given tuple only if the sum of askkey value of each and every characters present inside the string is greater than 500 using packing.


"""def fname(*r):
    l = []
    for i in a:
        s = 0
        if type(i) == str:
            for j in i:
                s += ord(j)
            if s > 500:
                l.append(i)

    print(r)  
    print(l)  

fname('aimI',23, 'ayantika',45,'raja','anand')
"""
# WAP to extract key value pairs from the dictionary only if length of key is exactly equal to three and value is of list collection using double packing.
"""
def fname(**d):
    f={}
    for k in d:
        if len(k)==3 and type(d[k])==list:
            f[k]=d[k]
    print(d)
    print(f)
fname(kkk=[10,20,30],k2=20)
"""

# WAP to extract key value pairs from the dictionary only if key and values are exactly equal.
"""

def ext(**d):
    f={}
    for k in d:
        if k == d[k]:
            f[k]=d[k]
    print(d)
    print(f)                    
ext(a='a', b=2, x='x', one=1)

"""
"""
# example of unpacking...

s='Anand is good boy'
print(*(reversed(s.split())))

# unpacking simple program
def fname(a,b,c):
    print(a,b,c)
fname(*(10,20,30))
"""
# 
def gg(d):
    for k,v  in d.items():
        print(f'{k}={v}')
d={'a':10,'b':20,'c':30}
gg(d)

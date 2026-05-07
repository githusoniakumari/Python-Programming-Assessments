
"""
#------------question 1------------------

def count_uppercase():
    s=input("enter the string: ")
    count=0
    for i in range(len(s)):
        if 'A'<=s[i]<='Z':
            count=count+1
    print(count)
count_uppercase()

#-------------2nd question---------------

input:- 'Ee sala cup Namde'
o/p:-   {'Ee': 2, 'cup': 3}

s='Ee sala cup Namde'.split()

d={}
for i in range(len(s)):
    if i%2==0:
        d[s[i]]=len(s[i])
print(d)

"""


"""

# day function 2nd part
# s='user defined function'
#o/p: {'user': 'ue', 'defined': 'eie', 'function': 'uio'}

def fname(s):
    s='user defined function'.split()
    d={}
    for i in s:
        t=''
        for j in i:
            if j in 'aeiouAEIOU':
                t+=j
                d[i]=t
    print(d)
s='user defined function'
fname(s)
"""

"""
# question 3:

# i/p: s='Python is Easy* for all branch'
# o/p: {'Python':'pn','is':' ','Easy*':'s','for':'o','all':'l','branch':'bh'}

 
def fname(s):
    a = s.split()
    
    d = {}
    
    for word in a:
        if word == 'Python':
            d[word] = word[0] + word[-1]   
        if word == 'is':
            d[word] = ' '                  
        if word == 'Easy*':
            d[word] = 's'                  
        if word == 'for':
            d[word] = 'o'                 
        if word == 'all':
            d[word] = word[-1]            
        if word == 'branch':
            d[word] = word[0] + word[-1]   
    
   
    print(d)


s = 'Python is Easy* for all branch'
fname(s)

"""

"""
# question 4:

# i/p: s='Python is@ Easy* for all branch'
# o/p: {'Python':'pn','is@':'s','Easy*':'s','for':'o','all':'l','branch':'bh'}

def fname(s):
    a = s.split()
    d = {}
    for word in a:
        if word == 'Python':
            d[word] = word[0] + word[-1]
        elif word == 'is@':
            d[word] = 's'
        elif word == 'Easy*':
            d[word] = 's'
        elif word == 'for':
            d[word] = 'o'
        elif word == 'all':
            d[word] = word[-1]
        elif word == 'branch':
            d[word] = word[0] + word[-1]
    print(d)

s = 'Python is@ Easy* for all branch'
fname(s)

"""

"""
# question 5:
# i/p: 'hi hello how are you'
# o/p: 'you are how hello hi'
def fname(s)
    s='hi hello how are you'
    a=s.split()
    a.reverse()
    print(' '.join(a))
s='hi hello how are you'
fname(s)
"""

"""
# dated :- 07-04-2025
# WAP TO EXTACT ALL THE STRING DATA ITEMS FROM THE GIVEN LIST AND JOIN THEM WITH THE HELP OF '*'
def fname():
    L=['anand',12.3,'rama',1,2+4j]
    # l=eval(input('enter a list: '))
    a=[]
    for i in L:
        if type(i)==str:
            #out.append(i)
            a+=[i]
    return '*'.join(a)
print(fname())
"""

"""

#i/p:- s1: '101011101100'
#i/p:- s2: '000110001011'

#o/p:- 4
def fname():
    s1='101011101100'
    s2='000110001011'
    count=0
    for i,j in zip(s1,s2):
        if i==j:
            count+=1
    return count
print(fname())
"""
"""
# i.p:-  a=[100,200,500,700,300,500,1000,800]

# i.p:- b=1000

# out :- [[200,800],[500,500],[700,300]]



def fname(b):
    a = [100, 200, 500, 700, 300, 500, 1000, 800]
    result = []
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == b:
                result.append([a[i], a[j]])
    return result


b = 1000
print(fname(b))
"""

# WAP to extract only digits from a string

string=input('enter a string: ')
l=[]
for i in string:
    if i.isdigit():
        l.append(i)
print(l)


  
    













            

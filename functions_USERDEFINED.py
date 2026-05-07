'''

def count_uppercase():
    string=input('enter a string: ')
    count=0
    if 'A'<=string<='Z':
        count+=1
        print(count)
count_uppercase()

'''

'''
WROMG OUTPUT
#input:- 'Ee Sala cup Namde'
#ouput:-{'Ee':2,'cup':3}
def fname():
    s = 'Ee sala cup Namde'.split()
    dic = {}
    for i in range(len(s)):
        if i % 2 == 0:
            dic[str(s[i])+  qa1]=len(s)
    
    print(dic)

fname()
'''

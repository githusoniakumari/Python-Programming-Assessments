"""
#1. WAP TO EXTACT ONLY DIGITS FROM THE STRING
def fname(s):
    words = s.split()        
    words.reverse()          
    return ' '.join(words)   

a = 'just looking like a wow'
b = fname(a)
print("Output:", b)
"""

"""

#2.
def midval_dict(s):
    dic = {}
    for i in s:
        if len(i) % 2 == 1:
            dic[i] = i[len(i) // 2]
        else:
            dic[i] = i[0] + i[-1]
    return dic

b = input("Enter the string: ").split()
output = midval_dict(b)
print("Output:", output)

"""

"""
#3. 
def fname(x):
    L = []
    dic = {}

    for i in x:
        a, b = i.split('.')
        L.append(b)

        if b not in dic:
            dic[b] = []
        dic[b].append(a)

    return L, dic


x = eval(input('enter a list: '))
#x=['jiocinema.com', 'file1.py', 'file.html', 'file2.py']

out1, out2 = fname(x)

print("Out1:", out1)
print("Out2:", out2)
"""

#4.
# doubt
"""
#5

def fname(s):
    chars = list(s)
    even = []
    odd = []

    for i in range(0, len(chars), 2):
        even.append(chars[i])
    for i in range(1, len(chars), 2):
        odd.append(chars[i])

    return ''.join(even + odd)

x = input("Enter a word: ")
out = fname(x)
print("Out:", out)



#6
def fname(s):
    freq = {}
    res = ""
    done = []  

    for ch in s:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1

    for ch in s:
        if ch not in done:
            res = res + ch + str(freq[ch])
            done.append(ch)

    return res

x = input("Enter the string: ")
out = fname(x)
print("Out:", out)
"""






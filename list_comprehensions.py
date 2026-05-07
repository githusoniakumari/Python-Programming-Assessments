#-----------------------------------------------------COMPREHENSIONS-----------------------------------------------------#  
"""
# 1. List comprehensions 
#WAP TO PRINT [(1, 2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,2),(3,3),(3,4)]

input=[(1, 2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,2),(3,3),(3,4)]
output=[(x, y) for (x, y) in input if x != y]

# Print the output
print(output)


#2. 
inp = 'Happy New YearA aaa'
# o/p = ['Happy',1],['New',0],['YearA',1],['aaa',3]

# Solution:

lip = inp.split()
print([[i, i.count('a')] for i in lip])


# 3.

inp='Python is very very Easy'

# o/p = [('Python',6), ('is',2), ('very',4), ('very',4), ('Easy',4)]

output = [(word, len(word)) for word in inp.split()]
print(output)


#4.
inp=[10,'hai',3.0,5+9j,{'a':1,'b':2}]
#o/p: [1, 3, 1, 1, 2]
output = [len(i) if type(i) in (str, dict, list, tuple, set) else 1 for i in inp]

print(output)


#5. WAP to extract all the complex numbers from the tuple given.

inp = (1, 2, 3+4j, 5.0, 'hello', 6+7j, [1, 2], {1: 'a', 2: 'b'}, (8+9j, 10))
print([i for i in inp if isinstance(i, complex)])


#6. WAP to find the cube of all numbers between the range 20 to 70 or 30 to 90 only if it is multiple of 5.

var = [i**3 for i in range(30,91) if i % 5 == 0]
print(var)

"""

#---------------------------------------------------------Dated: 23-06-2025--------------------------------------------------------------------#

#--------------------------------Dictionary Comprehensions--------------------------------#
"""
#1. WAP create a dictionary where n natural numbers should be the keys and the square of natural nos should be the values.


n = 10
output = {i: i**2 for i in range(1, n+1)}
print(output)


print({i: i**2 for i in range(1, 11)})


# ip:['a', 'b', 'c', 'd'] [1,2,3,4] o/p:[('a': 1), ('b': 2), ('c': 3), ('d': 4)]

input1 = ['a', 'b', 'c', 'd']
input2 = [1, 2, 3, 4]
output = {input1[i]: input2[i] for i in range(len(input1))}
print(output)

# ip:'HaiHeLlO' op: {'H':72,'L':76,'O':79}
input_str = 'HaiHeLlO'
output = {char: ord(char) for char in input_str if char.isupper()}
print(output)

# ip: L1=['a',8,3.4,[6,4],89] L2=[10,3.4,';hello',9,[5,6]] o/p: {'a':10, 8: 3.4, 3.4:'hello',89: [5,6]}
inp1 = ['a', 8, 3.4, [6, 4], 89]
inp2 = [10, 3.4, ';hello', 9, [5,6]]

output = {inpt1[i]: inp2[i] for i in range(len(inp1)) if isinstance(inp1[i], (int, float, str, tuple))}
print(output)



#ip: range(1,7) 
#op:{1:1,2:4,3:27,4:16,5:125,6:36}
output = {i:i**3 if i % 2 != 0 else i**2 for i in range(1,7)}
print(output)

"""

"""
#----------------------------------------------------------SET COMPREHENSIONS-------------------------------------------------------------------#

# WAP to find square of all even and cube of all odd nos between the range 60 to 120 and store the output in the form of set collection.
output = {i**2 if i % 2 == 0 else i**3 for i in range(60,121)}
print(output)

# WAP to extract all prime nos between 1 to n in the form of set collection.

#n = int(input("Enter the value of n: "))

prime_set = {x for x in range(2, 21) if all(x % d != 0 for d in range(2, x))}

#print("Prime numbers from 1 to", n, "are:", prime_set)
print(prime_set)

"""
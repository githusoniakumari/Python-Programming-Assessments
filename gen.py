#------------------------------------------------------GENERATORS--------------------------------------------------------#
#Example 1: Generator Function

# def sam():
#     print('hello')
#     yield 1
#     print('hi')
#     yield 2
#     print('bye bye')
#     yield 3
# print(sam())
# print(tuple(sam())) # list,set,tuple


#1. WAP to extract all the integers numbers from the given list:

# def extract_integers(lst):
#     for i in lst:
#         #if type(item) == int:
#         if isinstance(i , int):
#             yield i

# print(list(extract_integers([1, 2, 3, 4.3, ['hello', 3.1]])))

#2. WAP to get the following output: 
# inp= [10,7.8,323,4+5j,1111,78]

# out=[(323,3),(1111,4)]


# def fname(inp):
#     for i in inp:
#         if (isinstance(i,int) and str(i)==str(i)[::-1]):
#             yield(i,len(str(i)))
# inp= [10,7.8,323,4+5j,1111,78]
# print(list(fname(inp)))


# 3 WAP to create a generator function to generate factorial numbers between the range 1 to 100 and store the output in the form of tuple.
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
    
# def fact_generator():
#     for i in range(1,101):
#         yield (i,fact(i))
# print(tuple(fact_generator()))


# 4. Generator: Multiplication Table of n (Output: list)

# def multiplication_table_gen(n):
#     for i in range(1, 11):
#         yield n * i

# print("\nMultiplication Table of 5:")
# print(list(multiplication_table_gen(5)))




# 5. Generator: Prime Numbers (1 to 100)
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def prime_number_generator():
#     for i in range(1, 101):
#         if is_prime(i):
#             yield i

# print("\nPrime Numbers from 1 to 100:")
# print(list(prime_number_generator()))


# 6. Generator: Perfect Numbers (1 to 15)
# def is_perfect(n):
#     return sum(i for i in range(1, n) if n % i == 0) == n

# def perfect_number_generator():
#     for i in range(1, 16):
#         if is_perfect(i):
#             yield i

# print("\nPerfect Numbers from 1 to 15:")
# print(list(perfect_number_generator()))


# 7. Generator: Character : ASCII Value Dictionary
# def char_ascii_gen(s):
#     for ch in s:
#         yield (ch, ord(ch))

# print("\nCharacter to ASCII Dictionary for 'Hello123':")
# print(dict(char_ascii_gen("Hello123")))


# 8. Generator: Square of Integers if Palindrome
# def square_palindrome_gen(lst):
#     for i in lst:
#         if isinstance(i, int) and str(i) == str(i)[::-1]:
#             yield i ** 2

# print("\nSquare of Palindromic Integers:")
# print(list(square_palindrome_gen([121, 131, 22, 10, 44, 123])))






 
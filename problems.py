#1. WAP to check whether the collection is homogeneous or not using while without using break and continue...

"""

def is_homogeneous(collection):
    i = 1
    same_type = True

    while i < len(collection):
        if type(collection[i]) != type(collection[0]):
            same_type = False
        i += 1

    return same_type


my_list = eval(input('enter the list:'))   

''if is_homogeneous(my_list):
    print("The collection is homogeneous.")
else:
    print("The collection is not homogeneous.")
"""


#2. wap to print all the perfect no's between a range 1 to 1000.
"""
def is_perfect(num):
    i = 1
    sum_of_divisors = 0

    while i < num:
        if num % i == 0:
            sum_of_divisors += i
        i += 1

    return sum_of_divisors == num

n = 1
while n <= 1000:
    if is_perfect(n):
        print(n)
    n += 1
"""


def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==n:
        return True
    else:
        return False
perfect(n)
    
def new_perfect():
    for i in range(1, 1001):
        if perfect(i)==True:
            print(i)
new_perfect()
        



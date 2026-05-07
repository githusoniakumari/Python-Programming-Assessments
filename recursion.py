# sum of n natural nos.
"""
def sum_natural(n):
    if n==1:
        return 1
    return n+sum_natural(n-1)
print(sum_natural(7))

"""

# sum of fibonacci series

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

nterms=int(input("enter the no of terms:"))
for i in range(nterms):
    print(fibo(i))
# wap to extract all the string data items present inside the list collection using recursion.

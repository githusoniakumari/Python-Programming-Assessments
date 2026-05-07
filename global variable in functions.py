
# concept of global variable
"""

a,b=18,7
def ipl():
    global a
    a=45
    print(a)
print(a)
a=12
print(a)
ipl()
print(a)

"""
# concept of local variable

def outer():
    a=10
    print(a)
    a=100
    print(a)

    def inner():
        a=1000
        print(a)
        
    inner()
    print(a)
outer()

"""
def greeting(first, last):
  def getFullName():
    return first + " " + last

  print("Hi, " + getFullName() + "***")

greeting('***Anand Mohan', 'Jha')
"""


                                                    

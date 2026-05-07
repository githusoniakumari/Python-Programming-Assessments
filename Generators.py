#----------------------------------------------------------GENERATORS-----------------------------------------------------------#
def sam():
    print('hi')
    yield 1
    print("hello")
    yield 2
    print("Bye")
    yield 3
print(sam())
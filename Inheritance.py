class Parent:
    a=10
    b=20
    
    def __init__(self,c,d):
        self.c=c
        self.d=d
        
    def disp(self):
        print(self.a,self.b,self.c,self.d)
        
class Child(Parent):
    e=20
    f=50
    
        
    def __init__(self,g,h,c,d):
        self.g=g
        self.h=h
        self.c=c
        self.d=d
        
    def dispC(self):
        print(self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h)
        
ob=Child(100,200,300,400)
ob.disp()
ob.dispC()
     
    
    
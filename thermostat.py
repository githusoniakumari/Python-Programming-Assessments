class Brightness:
    def init(self,b=0):
        self.b=b
        
        
    def turn_off(self):
        self.b=0
        print('Light is turned off....')
        
        
    def turn_on(self):
        self.b=100
        print('Light is turned on....')
        
    def set_b(self,new):
        if self.b:
            self.b=new
            print(f'Your brightness is set to {set.b}%')
        else:
            print('Turn on light first...')


class Temperature:
        
    def init(self,temp=35):
        self.temp=temp
    
    def inc_temp(self):
        self.temp+=1
        print(f'current temperature is {self.temp} deg C')
        
    def dec_temp(self):
        self.temp-=1
        print(f'current temperature is {self.temp} deg C')
    
    def set_temp(self,new):
        self.temp=new
        print(f'current temperature is {self.temp} deg C')
        
class Thermostat(Brightness,Temperature):
    
    def init(self,bright=0,temp=20):
        Brightness.init(self,bright)
        Temperature.init(self,temp)
    
    def status(self):
        print(f'current brightness is {self.bright}%')
        print(f'current temperature is {self.temp}deg C')
        
ob=Thermostat()
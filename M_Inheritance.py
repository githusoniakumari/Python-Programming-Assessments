class Bank:
    b_name='Bondhon Bank'
    b_loc='Russia'
    b_ifsc='BND6000'
    
    def __init__(self,name,ph,pin):
        self.name=name
        self.ph=ph
        self.pin=pin
        self.bal=0
    
    
class ATM(Bank):
    atm_loc='Sector V'
    
    
    def ch_bal(self):
        upin=int(input("enter the pin to check the balance: "))
        
        if upin==self.pin:
            print('Available Balance: ',self.bal)
        else:
            print('Invalid Pin:(')
            
    def deposit(self):
        upin=int(input("enter the pin to check the balance: "))
        
        if upin==self.pin:
            amt=int(input("enter the balance to deposit: "))
            
            self.bal+=amt
        else:
            print('Invalid Pin:(')

    def withdraw(self):
        upin = int(input("Enter the pin to withdraw: "))
        if upin == self.pin:
            amt = int(input("Enter the amount to withdraw: "))
            if amt > 0 and amt <= self.bal:
                self.bal -= amt
                print(f'Amount ${amt} is withdrawn from your amount.... Available balance is ${self.bal}')
                print('Thank You visit Again :)')
            elif amt > self.bal:
                print('----Tu Gareeb hai :(----')
                
            else:
                print('Invalid amount')
        else:
            print('Ghar Jao :(')

            
class User(ATM):
    
    def __init__(self,name,ph,pin):
        super().__init__(name,ph,pin)

ob=User('Anand Mohan Jha',62902379260,123)
ob.ch_bal()
    
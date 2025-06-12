#atm process will initiate after checking PIN is matching or not
class pin_checking():
    def __init__(self,current_balance=1000):
        self.current_balance=current_balance
        self.__security_pin=9807 #im privating it.so that no one can accessible this data
    def pin(self):
        while True:
            self.code=int(input("enter your pin number:"))
            if self.code==self.__security_pin:
                return True
            else:
                print("enter the correct code")

class atm(pin_checking):#inherited class pin checking to atm
    #i have initiated an account with balance with self to access it in methods
    def atm_menu(self): #method to display the atm menu
        print("\n ATM Menu:")
        print("1.balance check")
        print("2.amount deposit")
        print("3.amount withdraw")
        print("4.exit")
    def balance_check(self):
        print(f"your current balance is {self.current_balance}") #for balance check im using self.current balance
    def deposite_money(self):#money deposite
        amount=float(input("enter the amount to add:"))
        if amount>0:
            self.current_balance+=amount
            print(f"{amount} rupees added to your account and your current balance is {self.current_balance} rupees")
        else:
            print("invalid amount")
        return self.current_balance #to exit from method
    def money_withdraw(self):#money withdrawl
        amount=float(input("enter the amount to withdraw:"))
        if self.current_balance>0 and amount<=self.current_balance:
            self.current_balance-=amount
            print(f"{amount} rupees withdraw successfully")
        elif amount>self.current_balance:
            print("insufficient balance")
        else:
            print("invalid amount.try again")
        return self.current_balance
#i have added all my features in ATM and now im initiating ATM functionality
class atmwork(atm):#inherited class atm
    def start_atm(self): #method to run the atm program
        while True:#initiating infinite loop which is going to run continuously
            atm_mechine.pin()
            self.atm_menu() # firstly it will show menu
            choice=input("enter the option in (1-4):")
            if choice=='1':
                self.balance_check()
            elif choice=='2':
                self.current_balance=self.deposite_money() #if choice 2 current balance will be deposite money only
            elif choice=='3':
                self.current_balance=self.money_withdraw()#if choice 3 current balance will be money after money withdrawl
            elif choice=='4':
                print("thanks for banking with us.bye!")
                break#breaking atm function after all features
            else:
                print("invalid option. try again") #if option is not within the list 
#instantiation to create object for the class to access real data 
atm_mechine=atmwork()#objectname=classname, this is for atmwork() because this is the derived class or last class 
atm_mechine.start_atm()#here i want to run ATM functionality. so,im calling start_atm() method to use it.

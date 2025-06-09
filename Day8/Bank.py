from abc import ABC,abstractmethod

class Account(ABC):

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class SavingAccount(Account):
    
    __balance = 0

    def get_balance(self):
        #return self.__balance
        print("Available Balance is:",self.__balance)
    
    def deposit(self, amount):
        self.__balance += amount
        print("Deposited Amount is:", self.__balance)

    def withdraw(self,amount):
        if amount > self.__balance:
            print("No sufficient Amount")
        if amount < self.__balance:
            self.__balance -= amount
            print("Available Balance:",self.__balance)

class CurrentAccount(Account):

    __balance = 0
    withdraw_limit = 3000

    def get_balance(self):
        print("Available Balance is:",self.__balance)
    
    def deposit(self, amount):
        self.__balance += amount
        print("Deposited money is:",self.__balance)

    def withdraw(self,amount):
        if self.__balance + self.withdraw_limit < amount:
            print("Not sufficient balance")
        if self.__balance + self.withdraw_limit > amount:
            self.__balance -= amount
            print("Amount is: ",self.__balance) 

class Bank:
    owner = "Bank"
    accountNumber = 0
    account_type = "none"
    

    def __init__(self,x,y,account_type = "Saving"):
        self.owner = x
        self.accountNumber = y
        
        
        if account_type == "Saving":
            self.account = SavingAccount()
        if account_type == "Current":
            self.account = CurrentAccount()

    def display(self):
        print(f"{self.owner} = {self.accountNumber}")


print("====> Kavitha Account <======")
Kavitha = Bank("Kavitha",1,"Saving")
Kavitha.account.deposit(500)
Kavitha.account.withdraw(300)
Kavitha.account.get_balance()

print("====>Mahesh Account<====")
Mahesh = Bank("Mahesh",2,"Current")
Mahesh.account.deposit(1000)
Mahesh.account.withdraw(3000)
Mahesh.account.get_balance()









        

        
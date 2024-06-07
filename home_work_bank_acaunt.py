# Create a hierarchy of classes representing different types of bank accounts. Start
# with a base class called BankAccount. Then, create two subclasses,
# SavingsAccount and CheckingAccount. Each subclass should inherit from the
# BankAccount class.
# ● The BankAccount class should have the following attributes and methods:
# ○ Attributes: account_number, balance
# ○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
# ● The SavingsAccount class should inherit from BankAccount and have an
# additional attribute interest_rate. Override the deposit method to add
# interest to the balance when a deposit is made.
# ● The CheckingAccount class should inherit from BankAccount and have an
# additional attribute overdraft_fee. Override the withdraw method to deduct
# the overdraft fee if a withdrawal causes the balance to go below zero



from abc import ABC,abstractmethod
class BankAcaunt(ABC):
    
    @abstractmethod
    def deposit(self,money_plus):
        pass

    @abstractmethod
    def withdraw(self,money_minus):
        pass


    
    def __init__(self,acaunt_number,balance) -> None:
        self.acaunt_number = acaunt_number
        self.balance = balance

    def deposit(self,money_plus):
        if type(money_plus) == int and money_plus > 0 :
            self.balance += money_plus
            return self.balance
        else:
            raise TypeError
    
    def withdraw(self,money_minus):
        if type(money_minus) == int and 0 < money_minus < self.balance:
            self.balance -= money_minus
            return self.balance
        else:
            raise TypeError
        
    def get_balance(self):
        return self.balance
    

class SavingsAccaunt(BankAcaunt):
    def __init__(self, acaunt_number, balance,interest_rate) -> None:
        super().__init__(acaunt_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, money_plus):
        if type(money_plus) == int and money_plus > 0:
            self.balance += (money_plus + ((money_plus/100)*self.interest_rate))
            return self.balance
        else:
            raise TypeError

class CheckingAccount(BankAcaunt):
    def __init__(self, acaunt_number, balance,overdraft_fee) -> None:
        super().__init__(acaunt_number, balance)
        self.overdraft_fee = overdraft_fee
    
    def withdraw(self, money_minus):
        if type(money_minus) == int and 0 < money_minus < self.balance:
            self.balance -= (money_minus + ((money_minus/100)*self.overdraft_fee))
            return self.balance
        else:
            raise TypeError


# accaunt_1 = BankAcaunt("david",1000)
# print(accaunt_1.deposit(150))
# print(accaunt_1.withdraw(200))

# accaunt_2 = CheckingAccount("David",2000,15)
# print(accaunt_2.withdraw(200))

a1  =BankAcaunt("david",2000)
print(a1.deposit(200))
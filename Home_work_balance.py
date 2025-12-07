# Define a class named BankAccount with an __init__ method that initializes two
# instance variables: account_holder and balance.
# The class has methods like deposit and withdraw, each of which takes an amount as
# an argument and updates the account balance accordingly. These methods also
# include checks for valid input and available funds.
# The get_balance method allows you to retrieve the account balance.
# We create an Object of the BankAccount class called account1 with an initial balance
# of $1000.
# We deposit $500 and withdraw $200 from the account and print the account
# information


 

class BankAccount:
    def __init__(self,accaunt_holder,balance) -> None:
        self.accaunt_holder = accaunt_holder
        self.balance = balance
    def deposit(self,money_plus):
        if money_plus > 0:
           self.balance += money_plus
           return self.balance
    def get_balance(self):
        return self.balance
    def withdraw(self,money_minus):
        if money_minus > 0:
            if self.balance < money_minus:
                print("not balance")
            else:
                self.balance -= money_minus
        else:
            print("wrong request")
        return self.balance
    
account1 = BankAccount("david",1000)
account1.withdraw(1500)
print(account1.balance)
# hello
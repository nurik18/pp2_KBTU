# 5
class BankAccount:           # 21 savage
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, income): 
        self.balance += income
        print(self.balance)


    def withdraw(self, outcome):
        if outcome > self.balance:
            print(f"Sorry, you don't have that much money on your balance. Your balance: {self.balance}")
        else:
            self.balance -= outcome
            print(self.balance)

acc1 = BankAccount("Tventi Van Savage", 1000000)

acc1.deposit(300000) 
acc1.withdraw(500000)
acc1.withdraw(1000000)
acc1.deposit(200000)
acc1.withdraw(1000000)
acc1.withdraw(1)
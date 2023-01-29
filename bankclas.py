class bankclas:
    balance = 0
    amount = 0

    def __init__(self,balance):
        self.balance = balance

    def set_amount(self,amt):
        self.amount = amt
    def deposit(self):
        self.balance += self.amount
    def check_balance(self):
        return "your account balance is : " +str(self.balance)
    def withdraw(self):
        if self.amount >=self.balance:
            msg = "insufficient balance"
        else:
            self.balance -= self.amount
            msg = "Transaction successful"
        print(msg)
        print("Your account balance is : " + str(self.balance))
    def transfer(self):
        if self.amount >=self.balance:
            msg = "Insufficient fund"
        else:
            self.balance -= self.amount
            msg = "Transaction successful"
        print(msg)
        print("Your account balance is : " + str(self.balance))

# transc1 = bankclas(0)
# transc1.set_amount(500)
# transc1.deposit()
# print(transc1.check_balance())
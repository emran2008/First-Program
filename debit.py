class account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    def debit(self,amount):
            self.balance -= amount
            print("rs.",amount,"is debited:", )
            print("Remaining balance:", self.get_balance())
    def credit(self,amount):
            self.balance += amount
            print("rs.",amount,"is credited:", )
            print("Remaining balance:", self.get_balance())
    def get_balance(self):
        return self.balance
acc1 = account(1000, 123456)

acc1.credit(200)
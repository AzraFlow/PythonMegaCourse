class Account:
    def __init__(self, filepath):
        self.fileid = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.fileid, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


# account = Account('balance.txt')
# print(account.balance)
# account.deposit(200)
# print(account.balance)
# account.commit()

checking = Checking("balance.txt", 1)
print(checking.balance)
checking.transfer(110)
print(checking.balance)
checking.commit()

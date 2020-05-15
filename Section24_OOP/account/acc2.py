class Account:
    def __init__(self, filepath):
        self.fileid = filepath  # instance variable
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
    """This class generates checking account object"""
    type = 'checking'  # class variable

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

jacks_checking = Checking("jack.txt", 1)
jacks_checking.transfer(50)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)

johns_checking = Checking("john.txt", 1)
johns_checking.transfer(50)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.type)

print(johns_checking.__doc__)

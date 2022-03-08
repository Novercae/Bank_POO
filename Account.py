from abc import abstractmethod, ABC

class Account(ABC):
    def __init__(self, agency, account, balance):
        self.agency = agency
        self.account = account
        self.balance = balance

    def info(self):
        print(f'Agency: {self.agency} '
            f'Account: {self.account} '
            f'Balance: {self.balance} ')

    def deposit(self, value):
        self.balance += value
        self.info()

    @abstractmethod
    def withdraw(self, value): pass


class Saving_Acc(Account):  # saving account, with no credit
    def withdraw(self, value):
        if self.balance < value:
            print('Insufficient funds.')
            return
            
        self.balance -= value
        self.info()
   
   
class Checking_Acc(Account):    # checking account, with credit
    def __init__(self, agency, account, balance, credit=100):
        super().__init__(agency, account, balance)
        self.credit = credit

    def withdraw(self, value):
        if (self.balance + self.credit) < value:
            print('Insufficient funds.')
            return

        self.balance -= value
        self.info()
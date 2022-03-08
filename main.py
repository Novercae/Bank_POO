from Bank import Bank
from Client import Client
from Account import Checking_Acc, Saving_Acc

bank = Bank()

client1 = Client("Lucas", 44)
client2 = Client('Pedro', 23)
client3 = Client('Júlia', 22)

account1 = Saving_Acc(1234, 234556, 0)
account2 = Checking_Acc(4242, 344345, 0)
account3 = Saving_Acc(2222, 454677, 0)

client1.insert_account(account1)
client2.insert_account(account2)
client3.insert_account(account3)


bank.insert_client(client1)
bank.insert_account(account1)

bank.insert_client(client2)
bank.insert_account(account2)

if bank.check(client1):
    client1.account.deposit(0)
    client1.account.withdraw(20)
else:
    print('Client not found.')

print("####################")

if bank.check(client2):
    client2.account.deposit(0)
    client2.account.withdraw(20)
else:
    print('Client not found.')
# Bank_POO
A code to create a bank.

Exercise with Abstraction, Inheritance, Encapsulation and Polymorphism
Create a banking system (extremely simple) that has customers, accounts and
a bank. The idea is that the customer has an account (savings or checking account) and that
can withdraw/deposit to this account. Current accounts have an extra limit. Bank
have customers and accounts.

Tips:
Create Customer class that inherits from Person class (Inheritance)
    Person has name and age (with getters)
    Customer TEM account (Aggregation of the ContaCorrente or ContaPoupanca class)
Create classes ContaSaupanca and ContaCurrent that inherit from Conta
    Current Account must have an extra limit
    Accounts have branch, account number and balance
    Accounts must have a deposit method
    Account (super class) must have abstract withdraw method (Abstraction and
    polymorphism - the subclasses that implement the draw method)
Create Bank class to AGGREGATE customer and account classes (Aggregation)
Bank will be responsible for authenticating the customer and accounts as follows:
    Bank has accounts and customers (Aggregation)
    * Check if the branch is from that bank
    * Check if the customer is from that bank
    * Check if the account is from that bank
It will only be possible to withdraw if you pass the bank authentication (described above)

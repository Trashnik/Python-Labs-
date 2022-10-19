
class BankAccount:

    def __init__(self, balance: int = 0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,value):
        self.__balance = value

    def deposit(self, amount): 
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance




b1 = BankAccount()

balance = int(input("First deposit: "))
b1.set_balance(balance)

check = True

while check:
    print(f"1: Deposit\n2: Withdraw\n3: Check balance")
    choose = int(input("Choose the operation: "))
    if choose == 1:
        deposit = int(input("Deposit: "))
        b1.deposit(deposit)
    if choose == 2:
        withdraw = int(input("Withdraw: "))
        b1.withdraw(withdraw)
    if choose == 3:
        check = False
print(f"Balance = {b1.get_balance()}")
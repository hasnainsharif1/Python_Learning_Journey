class  bank_account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance #its private varialbe

    def desposite(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. Now balance is {self.__balance}")
    
    def get_balance(self):
        return self.__balance

account =  bank_account("1234", 5000)

account.desposite(3000)
print(account.get_balance())

# print(account.__balance)
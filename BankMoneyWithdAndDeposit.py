class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount!"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. Remaining balance: {self.balance}"
        return "Insufficient funds or invalid amount!"

    def check_balance(self):
        return f"Account {self.account_number} Balance: {self.balance}"


acc = BankAccount("12345", 1000)
print(acc.deposit(500))  
print(acc.withdraw(200))  
print(acc.check_balance())   

acc = BankAccount("37591", 5000)
print(acc.deposit(1000))  
print(acc.withdraw(7000))  
print(acc.check_balance())   


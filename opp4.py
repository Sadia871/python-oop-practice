class Bank:
    bank_name = "Global Bank"
    total_accounts = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        Bank.total_accounts += 1

    def display_account_info(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"
        

    @classmethod
    def display_bank_info(cls):
        return f"Bank Name: {cls.bank_name}, Total Accounts: {cls.total_accounts}"
# Create objects
account1 = Bank("Alice", 1000)
account2 = Bank("Bob", 1500)
account3 = Bank("Charlie", 2000)
account4 = Bank("Diana", 2500)
# Call methods  
print(account1.display_account_info())
print(account2.display_account_info())
print(account3.display_account_info())
print(account4.display_account_info())  
print(Bank.display_bank_info())

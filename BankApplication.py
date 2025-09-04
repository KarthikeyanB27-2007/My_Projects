#Create a bank application with basic functionalities like account creation, deposit, withdrawal, and balance inquiry using Object-Oriented Programming principles in Python.

class Bank:
    bank_name = "Brendon-Madhesh Syndicate International Bank"
    bank_loc = "Avadi,Channai"
    bank_branch  = "Avadi Main Branch"
    bank_owner = "Madhesh.B"
    bank_IFSC = "BMSI0001"

    def create_account(self, name, acc_no, acc_type, balance):
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance
        print(f"Account created for {self.name} with account number {self.acc_no} and balance {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawed {amount}. Current balance is {self.balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount")

    def balance_inquiry(self):
        print(f"Balance check for {self.name}, Your current balance is {self.balance}")

# Creating an instance of the Bank class
customer1 = Bank()
customer1.create_account("Karthikeyan", "123456789", "Savings", 10000000)
customer1.deposit(50000)
customer1.balance_inquiry()    

customer2 = Bank()
customer2.create_account("Madhesh", "987654321", "Current", 200000)
customer2.withdraw(150000)
customer2.balance_inquiry() 

customer3 = Bank()
customer3.create_account("Kishore", "456789123", "Savings", 5000000)
customer3.withdraw(40000)
customer3.balance_inquiry()

print(Bank.bank_name,Bank.bank_loc,Bank.bank_branch,Bank.bank_owner,Bank.bank_IFSC)

customer1.bank_name = "Brendon-Madhesh Syndicate International Bank - Avadi"
print(customer1.bank_name,customer1.bank_loc,customer1.bank_branch,customer1.bank_owner,customer1.bank_IFSC)

print(customer2.bank_name,customer2.bank_loc,customer2.bank_branch,customer2.bank_owner,customer2.bank_IFSC)
print(customer3.bank_name,customer3.bank_loc,customer3.bank_branch,customer3.bank_owner,customer3.bank_IFSC)

Bank.bank_name = "Brendon-Madhesh Syndicate International Bank - Chennai"
print(Bank.bank_name,Bank.bank_loc,Bank.bank_branch,Bank.bank_owner,Bank.bank_IFSC)
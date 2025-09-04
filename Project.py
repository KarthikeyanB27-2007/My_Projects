import tkinter as tk
from tkinter import messagebox

class Bank:
    bank_name = "Welcome to Brendon-Madhesh Syndicate International Bank"
    bank_loc = "Avadi, Chennai"
    bank_branch = "Avadi Main Branch"
    bank_owner = "Madhesh.B"
    bank_IFSC = "BMSI0001"

    def __init__(self):
        self.name = None
        self.acc_no = None
        self.acc_type = None
        self.balance = 0

    def create_account(self, name, acc_no, acc_type, balance):
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance
        return f"Account created for {self.name} with account number {self.acc_no} and balance {self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance is {self.balance}"
        else:
            return "Deposit amount must be positive"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn {amount}. Current balance is {self.balance}"
        else:
            return "Insufficient balance or invalid withdrawal amount"

    def balance_inquiry(self):
        return f"Balance check for {self.name}, Your current balance is {self.balance}"


# GUI Part
class BankApp:
    def __init__(self, root):
        self.bank = Bank()

        root.title("Bank Application")

        # Title Label
        title = tk.Label(
            root, 
            text=f"Welcome to {Bank.bank_name}", 
            font=("Arial", 16, "bold"), 
            fg="darkblue"
        )
        title.grid(row=0, column=0, columnspan=2, pady=10)

        # Labels & Entries
        tk.Label(root, text="Name").grid(row=1, column=0, sticky="w", padx=10)
        tk.Label(root, text="Account No").grid(row=2, column=0, sticky="w", padx=10)
        tk.Label(root, text="Account Type").grid(row=3, column=0, sticky="w", padx=10)
        tk.Label(root, text="Balance").grid(row=4, column=0, sticky="w", padx=10)
        tk.Label(root, text="Amount").grid(row=5, column=0, sticky="w", padx=10)

        self.name_entry = tk.Entry(root, width=30)
        self.acc_entry = tk.Entry(root, width=30)
        self.type_entry = tk.Entry(root, width=30)
        self.balance_entry = tk.Entry(root, width=30)
        self.amount_entry = tk.Entry(root, width=30)

        self.name_entry.grid(row=1, column=1, pady=2)
        self.acc_entry.grid(row=2, column=1, pady=2)
        self.type_entry.grid(row=3, column=1, pady=2)
        self.balance_entry.grid(row=4, column=1, pady=2)
        self.amount_entry.grid(row=5, column=1, pady=2)

        # Buttons
        tk.Button(root, text="Create Account", width=20, command=self.create_account).grid(row=6, column=0, pady=5)
        tk.Button(root, text="Deposit", width=20, command=self.deposit).grid(row=6, column=1, pady=5)
        tk.Button(root, text="Withdraw", width=20, command=self.withdraw).grid(row=7, column=0, pady=5)
        tk.Button(root, text="Balance Inquiry", width=20, command=self.balance_inquiry).grid(row=7, column=1, pady=5)

    def create_account(self):
        msg = self.bank.create_account(
            self.name_entry.get(),
            self.acc_entry.get(),
            self.type_entry.get(),
            int(self.balance_entry.get())
        )
        messagebox.showinfo("Info", msg)

    def deposit(self):
        msg = self.bank.deposit(int(self.amount_entry.get()))
        messagebox.showinfo("Info", msg)

    def withdraw(self):
        msg = self.bank.withdraw(int(self.amount_entry.get()))
        messagebox.showinfo("Info", msg)

    def balance_inquiry(self):
        msg = self.bank.balance_inquiry()
        messagebox.showinfo("Balance", msg)


if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
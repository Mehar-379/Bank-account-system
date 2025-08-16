
class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Name  : {self.account_name}")
        print(f"Balance       : ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number, account_name, balance)

    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f"Added ${interest} interest. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            interest_on_withdrawal = amount * 0.05
            self.balance -= interest_on_withdrawal
            print(f"Withdrew ${amount}. Interest on withdrawal: ${interest_on_withdrawal}. Current balance: ${self.balance}")

def main():
    account_number = input("Enter account number: ")
    account_name = input("Enter account name: ")
    balance = float(input("Enter initial balance: "))

    savings_account = SavingsAccount(account_number, account_name, balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Add interest")
        print("4. Display details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            savings_account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            savings_account.withdraw(amount)
        elif choice == "3":
            savings_account.add_interest()
        elif choice == "4":
            savings_account.display_details()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

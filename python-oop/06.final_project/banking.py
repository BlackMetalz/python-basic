from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def create_account(self, name, initial_deposit):
        return 0

    @abstractmethod
    def authenticate(self, name, account_number):
        pass

    @abstractmethod
    def withdraw(self, withdraw_amount):
        pass

    @abstractmethod
    def deposit(self, deposit_amount):
        pass

    @abstractmethod
    def display_balance(self):
        pass

class SavingsAccount(Account):
    def __init__(self):
        # [key][0] => name, [key][1] => initial_deposit
        self.savings_accounts = {}

    def create_account(self, name, initial_deposit):
        self.account_number = randint(10000, 99999)
        self.savings_accounts[self.account_number] = [name, initial_deposit]
        print("Account created successfully. Your account number is: {}".format(self.account_number))

    def authenticate(self, name, account_number):
        if account_number in self.savings_accounts.keys():
            if self.savings_accounts[account_number][0] == name:
                print("Authentication successful for account number: {}".format(account_number))
                self.account_number = account_number
                return True
            else:
                print("Authentication failed: Name does not match for account number: {}".format(account_number))
                return False
        else:
            print("Authentication failed: Account number does not exist.")
            return False

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.savings_accounts[self.account_number][1]:
            print("Insufficient funds for withdrawal.")
        else:
            self.savings_accounts[self.account_number][1] -= withdraw_amount
            print("Withdrawal successful")
            self.display_balance()

    def deposit(self, deposit_amount):
        self.savings_accounts[self.account_number][1] += deposit_amount
        print("Deposit successful")
        self.display_balance()

    def display_balance(self):
        print("Available balance: {}".format(self.savings_accounts[self.account_number][1]))


SavingsAccount = SavingsAccount()
while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to authenticate an existing account")
    print("Enter 3 to exit")
    user_choice = int(input())
    if user_choice == 1:
        name = input("Enter your name: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        SavingsAccount.create_account(name, initial_deposit)
    if user_choice == 2:
        name = input("Enter your name: ")
        account_number = int(input("Enter your account number: "))
        if SavingsAccount.authenticate(name, account_number):
            while True:
                print("Enter 1 to deposit")
                print("Enter 2 to withdraw")
                print("Enter 3 to check balance")
                print("Enter 4 to go back to previous menu")
                transaction_choice = int(input())
                if transaction_choice == 1:
                    deposit_amount = float(input("Enter deposit amount: "))
                    SavingsAccount.deposit(deposit_amount)
                elif transaction_choice == 2:
                    withdraw_amount = float(input("Enter withdrawal amount: "))
                    SavingsAccount.withdraw(withdraw_amount)
                elif transaction_choice == 3:
                    SavingsAccount.display_balance()
                elif transaction_choice == 4:
                    print("Going back to the main menu.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Authentication failed for {}. Cannot perform transactions.".format(name))
    elif user_choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")


class BankAccount:
    bank_name = "Bank of Gastonia"

    def __init__(self, customer_name, current_balance, minimum_balance, _account_number, __routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.account_number = _account_number
        self.routing_number = __routing_number

    def deposit(self, amount):
        self.current_balance = self.current_balance + amount
        print("Deposit complete!")

    def withdraw(self, amount):
        if amount > self.current_balance:
            print("Insufficient funds, withdrawal incomplete.")
        else:
            self.current_balance = self.current_balance - amount
            print("Withdrawal complete!")

    def print_customer_information(self):
        print(self.bank_name)
        print(f"Routing Number: {self.routing_number}")
        print(f"Account Number: {self.account_number}")
        print(self.customer_name)
        print(f"Current Balance: {self.current_balance}")


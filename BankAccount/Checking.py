from BankAccount import BankAccount

class Checking(BankAccount):


    def __init__(self, customer_name, current_balance, minimum_balance, _account_number, __routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, _account_number, __routing_number)

    def transfer(self, amount):
        transfer_limit = 500;
        if amount > transfer_limit:
            print("Transfer incomplete.")
        else:
            self.current_balance = self.current_balance + amount
            print("Transfer complete. Here is your updated balance:")
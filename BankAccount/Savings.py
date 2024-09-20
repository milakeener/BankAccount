from BankAccount import BankAccount

class Savings(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, _account_number, __routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, _account_number, __routing_number)

    def applyInterest(self):
        interest = 0.5
        self.current_balance = (self.current_balance * interest) + self.current_balance
        print("Interest applied. Here is your updated balance:")




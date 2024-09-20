from Savings import Savings
from Checking import Checking


# account1 = BankAccount("Claire", 250.0, 100.0)
# account1.deposit(100)
# account1.print_customer_information()
#
# account2 = BankAccount("Maria", 100.0, 100.0)
# account2.withdraw(200)
# account2.print_customer_information()

account3 = Checking("Maria", 100.0, 100,7764,  3324)
account3.print_customer_information()
account3.transfer(50)
account3.print_customer_information()

account4 = Savings("Claire", 20.0, 20.0, 8228, 1102)
account4.print_customer_information()
account4.applyInterest()
account4.print_customer_information()
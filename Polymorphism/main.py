from Banking_sys import Bank_Account, SavingsAccount

Alice = SavingsAccount("Alice", "SA123", 500, 0.03)

Alice.deposit(400, "House keeping money")

Alice.withdraw(810)
Alice.display_Account_Details()

Alice.withdraw(50)
Alice.display_Account_Details()
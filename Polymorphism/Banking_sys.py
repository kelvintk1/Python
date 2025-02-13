class Bank_Account:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = str(account_holder)
        self.account_number = str(account_number)
        self.balance = float(balance)

    def deposit(self,amount):
        self.balance += float(amount)
        print(f"Updated balance💵: {self.balance}")

    def deposit(self, amount, note):
        if isinstance(amount, int) or amount > 0:
            self.balance += float(amount)
            print(f"Current Balance💵: {self.balance}\nDeposit Successful✅")
            print(f"Note: {note}\n")
        else:
            raise ValueError("Make sure your input is a positive integer")

    def withdraw(self, amount):
        if isinstance(amount, int) or amount < 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal Successful✅\nCurrent Balance💵: {self.balance:.2f}")
            else:
                print(f"Insufficient fund❌\nCurrent Balance: {self.balance:.2f}")
        else:
            raise ValueError("Make sure your input is a positive integer")
        
    def display_Account_Details(self):
        print(f"Account holder: {self.account_holder}\nAccount number: {self.account_number}\nBalance💵: {self.balance:.2f}")

class SavingsAccount(Bank_Account):
    def __init__(self, account_holder, account_number, balance, interest_rate):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = float(interest_rate)

    def withdraw(self, amount):
        if isinstance(amount, int) and amount > 0:
            if self.balance > amount:
                if self.balance >= 100:
                    self.balance -= amount
                    print(f"Withdrawal Successful✅\nCurrent Balance💵: {self.balance:.2f}")
                elif self.balance < 100:
                    print(f"Sorry❌\nCurrent Balance: {self.balance:.2f}\nThe system does not allow you to withdraw when your balance is less than $100")
            elif self.balance < amount:
                print(f"Insufficient fund❌\nCurrent balance: {self.balance}")
        elif not isinstance(amount, int):
            raise ValueError("Make sure your input is a positive integer")
        else:
            print("Withdrawal failed❌")

    def calculate_Interest(self):
        return f"{self.balance * self.interest_rate:.2f}"
    
    def display_Account_Details(self):
        print(f"Account holder: {self.account_holder}\nAccount number: {self.account_number}\nBalance💵: {self.balance:.2f}\nInterest rate: {self.interest_rate}\n")


class Bank_system:
    def __init__(self, account_number, account_holder, balance, interest_rate):
        self.account_number = str(account_number)
        self.account_holder = account_holder
        if balance >= 0.0:
            self.balance = float(balance)
        else:
            print("Balance cannot be negative❌")
        if interest_rate >= 0.0 and interest_rate <= 1.0:
            self.interest_rate = float(interest_rate)
        else:
            print("Interest rate can only be between 0.0 and 1.0❌")
    
    def deposit(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Your input must be an integer❌")
        elif amount < 0:
            print("Amount cannot be less than 0❌")
        else:
            self.balance += int(amount)

    def withdraw(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Your input must be an integer❌")
        elif amount < 0:
            print("Amount cannot be less than 0❌")
        elif amount > self.balance:
            print(f"Insufficient funds❌\n You only have a balance of ${self.balance} in your account")
        else:
            self.balance -= amount

    def calculate_interest(self):
        return self.balance * self.interest_rate
    
    def get_balance(self):
        return self.balance
    
    def account_details(self):
        return f"Account number: {self.account_number}\nAccount holder: {self.account_holder}\nBalance💵: {self.balance:.2f}\nInterest rate: {self.interest_rate:.2%}"
    




from Banking_system import Banking_system

account_1 = Bank_Account("22017033", "Kelvin Tetteh K.", 9000.00, 0.07)

print(f"Account Details🧾:\n\n{account_1.account_details()}\n")

account_1.deposit(1000)
print(f"Updated Account Details🧾:\n{account_1.account_details()}\n")

account_1.withdraw(500)
print(f"Updated Account Details🧾:\n{account_1.account_details()}\n")

earned_interest = account_1.calculate_interest()
print(f"Annual Interest Earned💵: {earned_interest:.2f}")
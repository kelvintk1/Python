print("Welcome to the Tip Calculator!")
Tbill = int(input("What is the total bill?\n ₵"))
percent = int(input("What percentage would you like to give?\n %"))
people = int(input("How many people are to split the bill?\n"))

percentage = percent / 100
TotalBill = Tbill + percentage
peopleshare = round(TotalBill / people, 2)
share = str(peopleshare)
print("Each person is supposed to pay: " + share)

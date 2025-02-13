print("Welcome to the Leap year checker!\n")
year = int(input("Which year would you like to check?\n"))
length = len(str(year))

if length != 4:
    print("Sorry, your input is incorrect. It should be exactly 4 digits.\n")
    year = int(input("Which year would you like to check?\n"))
else:
    print("Let's see if it's a leap year...\n")

every = year % 4
excep = year % 100
unless = year % 400

def leap_year(year):
    if every == 0:
        if excep == 0:
            if unless == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
answer = leap_year(year)
print(answer)

# This is also works;
#if every == 0:
#    print("It is a leap year.\n")
#elif excep == 0:
#    print("It is not a leap year.\n")
#elif unless == 0:
#    print("It is a leap year.\n")
#else:
#   print("It is not a leap year.\n")

def days_in_month(Year, Month):
    Last_days = [30, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year) and Month == 2:
        return 29
    else:
        return Last_days[Month-1]
    
year = int(input("Enter a year:\n"))
month = int(input("Enter a month:\n"))
if month < 1 or month > 12:
    print("Sorry, your input should be between 1 and 12.")
days = days_in_month(year, month)
print(days)
                    


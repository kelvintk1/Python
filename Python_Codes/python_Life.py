# number of days, weeks, and months in a year.
days = 365
weeks = 52
months = 12
#standard life time
life = int(input("How long would you like to live? (years)\n"))
#standard days, weeks and months
sl_days = life * days
sl_weeks = life * weeks
sl_months = life * months

age = int(input("How old are you now?\n"))
#number of days, weeks and months spent with your age now.
A_days = days * age
A_weeks = weeks * age
A_monnths = months * age 
#number of days, weeks and months left.
R_days = sl_days - A_days
R_weeks = sl_weeks - A_weeks
R_months = sl_months - A_monnths

print(f"You have {R_days} days, {R_weeks} weeks and {R_months} months left")

intro = "Welcome to the email slicer.\n"
Intro = intro.title()
print(Intro)

email = input("Enter your email: \n")
email = email.strip()
slicer_index = email.index("@")
Username = email[:slicer_index]
domain_name = email[slicer_index+1:]
print(f"Your username is {Username}\nYour domain is {domain_name}.\n")

print("Who would be sacrifing tonight for the IA?☠️")
L_names= input("Give me everybody's name separated by a comma(,).\n")
names = L_names.split(", ")
# print(names)
N_names = len(names)
import random
R_number = random.randint(0, N_names-1)
kay =random.randrange(0,5)
payer = names[R_number]
print(f"{payer} would be sacrificing tonight.")




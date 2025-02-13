print("Welcome to the Ballot system!\n")
import random
ballot = []
group = input("Input the names of the groups:\n").split(", ")
ballot.extend(group)
print(ballot)
random.shuffle(ballot)

for position, group in enumerate(ballot, start=1):
    print(f"{group} is position number {position}")



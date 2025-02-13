print("Welcome to the Love Detector. \n")

for row in range(6):
    for col in range(7):
        if (row == 0 and (col % 3 != 0)) or \
           (row == 1 and (col % 3 == 0)) or \
           (row - col == 2) or \
           (row + col == 8):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

G_name = input("What is the name of the lady? \n")
M_name = input("What is the name of the gentleman?\n")

Cname = G_name + M_name
name = Cname.lower()

T = name.count("t")
R = name.count("r")
U = name.count("u")
E = name.count("e")

TrueT = T + R + U + E

L = name.count("l")
O = name.count("o")
V = name.count("v")
LE = name.count("e")

Love = L + O + V + LE

Score = str(TrueT) + str(Love)
Fscore = int(Score)

if Fscore < 10 or Fscore >90:
    print(f"Your score is {Fscore}; you go together like coke and mentos. \n")
elif Fscore > 40 and Fscore < 50:
    print(f"Your score is {Fscore}; you are alright together. \n")
else:
    print(f"Your score is {Fscore}; you guys should  stop wasting time.")




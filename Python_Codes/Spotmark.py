print("Welcome to the Treaasure Island. \n")

row_1 = ["☠️", "☠️", "☠️"]
row_2 = ["☠️", "☠️", "☠️"]
row_3 = ["☠️", "☠️", "☠️"]
map = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")

import random
R_column = random.randint(1, 3)
R_row = random.randint(1, 3)
r_row = map[R_row-1]

position = input("Predict the position of the treasure? \n Your input must be in numbers according to rows(1-3) and columns(1-3).\n")
column = position[0]
row = position[1]
Column = int(column)
Row = int(row)
Post = map[Row-1]

if R_column == Column and R_row == Row:
    r_row[R_column-1] = "💎"
    print(f"{row_1}\n{row_2}\n{row_3} \n Hurray! You found the hidden treasure.")
else:
    Post[Column-1] = "❌" 
    print(f"{row_1}\n{row_2}\n{row_3}")
    print("Sorry, the hidden treasure isn't there.\n")
    print("Instead, the hidden treasure is rather here\n")
    r_row[R_column-1] = "💎"
    print(f"{row_1}\n{row_2}\n{row_3}")
    

    








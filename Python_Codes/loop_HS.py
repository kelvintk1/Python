student_scores = input("Input the list of the students' scores.\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0 
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {score}\n")
total = 0
for n in range(1, 101, 2):
    print(n)
    total += n
print(total)


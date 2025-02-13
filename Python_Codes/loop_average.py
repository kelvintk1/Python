students_height = input("Input a list of students height. \n").split()
print("\n")
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
    print(f"{students_height[n]}")

length = len(students_height)
print(f"\nfrequency: {length}")
total = sum(students_height)
print(f"Sum: {total}")
average = round(total / length)
print(f"The average number of their heights is: {average}\n")

S_diff = [(n - average)**2 for n in students_height]
diffsum = sum(S_diff)
variance = round(diffsum / length,2)
print(f"The variance of those digits is: {variance}")
import math
SD = round(math.sqrt(variance),2)
print(f"The Stabdard Deviation of those digits is: {SD} ")



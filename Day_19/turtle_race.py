from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1000, height=700)

finish_line = Turtle(shape="blank")
finish_line.penup()
finish_line.goto(350, -150)
finish_line.pendown()
finish_line.lt(90)
finish_line.fd(400)

is_race_on = False

user_bet = screen.textinput(title="Make a bet", prompt="Which turtle🐢 will win the race🏎️? (blue, red, violet, orange) Enter the color:")
print(user_bet)

colors = ["red", "blue", "violet", "orange"]
y_positions = [100, 200, 0, -100]
all_turtles = []

for turtle_index in range(0, 4):
    new_turtles = Turtle()
    new_turtles.shape("turtle")
    new_turtles.color(colors[turtle_index])
    new_turtles.penup()
    new_turtles.goto(-470, y=y_positions[turtle_index])
    new_turtles.penup()
    all_turtles.append(new_turtles)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if user_bet not in colors:
            is_race_on = False
            print("Sorry❌ \n Make sure your input is accurate✅👍")
        elif turtle.xcor() > 350:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won 🥳👏\n The {winning_color} turtle🐢 won the race🏎️ ")
            else:
                print(f"You've lost😭\n The {winning_color} turtle🐢 won the race🏎️ ")

        speed = random.randint(0, 10)
        turtle.fd(speed)
    

screen.exitonclick()



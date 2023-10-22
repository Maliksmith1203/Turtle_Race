import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your Bet", prompt="Choose which color turtle will win the race")
print(user_bet)
colors = ["red", "blue", "green", "orange", "pink", "yellow"]
tim = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
tan = Turtle(shape="turtle")
tin = Turtle(shape="turtle")
ton = Turtle(shape="turtle")
toy = Turtle(shape="turtle")
turtles = [tim, tom, tan, tin, ton, toy]

def set_colors():
    for turtle in turtles:
        color = random.choice(colors)
        colors.remove(color)
        turtle.color(color)


def set_positions():
    x = -230
    y_positions = [-70, -40, -10, 20, 50, 80]
    i = 0
    for turtle in turtles:
        if i == 0:
            turtle.penup()
            turtle.goto(x=x, y=y_positions[i])

            i += 1
        else:
            turtle.penup()

            turtle.goto(x=x, y=y_positions[i])
            i += 1


set_colors()
set_positions()
game_on = False
if user_bet:
    game_on = True
while game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congrats you won the bet the winner is the {winning_color} turtle")
            else:
                print(f"Sorry you lost the bet the winner is the {winning_color} turtle")

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)
screen.exitonclick()

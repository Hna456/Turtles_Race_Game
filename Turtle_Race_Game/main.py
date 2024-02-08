from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cord = -100
is_game_on = False
user_input = screen.textinput("Do Your Bet!", "Which Colored Turtle Will Win? ")


all_turtle = []
for color in colors:
    t = Turtle(shape="turtle")
    t.penup()
    t.color(color)
    t.goto(-230, y_cord)
    y_cord += 40
    all_turtle.append(t)

if user_input:
    is_game_on = True

while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_input:
                print(f"You won! The winning turtle is {winning_turtle}.")
            else:
                print(f"You lost! The winning turtle is {winning_turtle}.")

        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)

screen.exitonclick()

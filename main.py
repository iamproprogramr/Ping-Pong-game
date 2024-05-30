# This program is written by Muhammad Yousaf
# Email: yousafsahiwal3@gmail.com

import turtle

# Set up the game window
screen = turtle.Screen()
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle A
a = turtle.Turtle()
a.speed(0)
a.shape("square")
a.color("blue")
a.shapesize(stretch_wid=6, stretch_len=1)
a.penup()
a.goto(-350, 0)

# Paddle B
b = turtle.Turtle()
b.speed(0)
b.shape("square")
b.color("red")
b.shapesize(stretch_wid=6, stretch_len=1)
b.penup()
b.goto(350, 0)

# Ball
boll = turtle.Turtle()
boll.speed(1)
boll.shape("circle")
boll.color("yellow")
boll.penup()
boll.goto(0, 0)
boll.dx = 0.2
boll.dy = -0.2

# Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function to move paddle A up
def paddle_a_up():
    y = a.ycor()
    if y < 250:
        y += 20
    a.sety(y)

# Function to move paddle A down
def paddle_a_down():
    y = a.ycor()
    if y > -240:
        y -= 20
    a.sety(y)

# Function to move paddle B up
def paddle_b_up():
    y = b.ycor()
    if y < 250:
        y += 20
    b.sety(y)

# Function to move paddle B down
def paddle_b_down():
    y = b.ycor()
    if y > -240:
        y -= 20
    b.sety(y)

# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    screen.update()

    # Move the ball
    boll.setx(boll.xcor() + boll.dx)
    boll.sety(boll.ycor() + boll.dy)

    # Border checking
    if boll.ycor() > 290:
        boll.sety(290)
        boll.dy *= -1

    if boll.ycor() < -290:
        boll.sety(-290)
        boll.dy *= -1

    if boll.xcor() > 390:
        boll.goto(0, 0)
        boll.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if boll.xcor() < -390:
        boll.goto(0, 0)
        boll.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (340 < boll.xcor() < 350) and (b.ycor() - 50 < boll.ycor() < b.ycor() + 50):
        boll.setx(340)
        boll.dx *= -1

    if (-350 < boll.xcor() < -340) and (a.ycor() - 50 < boll.ycor() < a.ycor() + 50):
        boll.setx(-340)
        boll.dx *= -1

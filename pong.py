import turtle

# Set up the game window
win = turtle.Screen()
win.title("Pong Project")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle settings
def create_paddle(x, shape, color):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape(shape)
    paddle.color(color)
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, 0)
    return paddle

paddle_a = create_paddle(-350, "square", "white")
paddle_b = create_paddle(350, "square", "white")

# Ball settings
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# Pen for displaying scores
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Function to update the score display
def update_score():
    pen.clear()
    pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# Function to move paddles
def move_paddle(paddle, direction):
    y = paddle.ycor()
    y += direction
    paddle.sety(y)

# Keybindings
win.listen()
win.onkeypress(lambda: move_paddle(paddle_a, 20), "w")
win.onkeypress(lambda: move_paddle(paddle_a, -20), "s")
win.onkeypress(lambda: move_paddle(paddle_b, 20), "Up")
win.onkeypress(lambda: move_paddle(paddle_b, -20), "Down")

# Initialize scores for both players
score_a = 0
score_b = 0

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        update_score()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        update_score()

    # Paddle and Ball Collisions
    if (
        340 > ball.xcor() > 330
        and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50
    ):
        ball.setx(340)
        ball.dx *= -1

    if (
        -340 < ball.xcor() < -330
        and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50
    ):
        ball.setx(-340)
        ball.dx *= -1

import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game by.V")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#border for game
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("black")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#head of snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food_colors = random.choice(['red', 'blue', 'green', 'yellow', 'purple'])
food_shape = random.choice(['circle'])
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(20, 20)

#score
scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.shape("circle")
scoreBoard.color("white")
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, 250)
scoreBoard.write("Score: 0 High Score: 0", align="center", font=("Courier", 25, "normal"))

#key functions
def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":  
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(moveUp, "w")
wn.onkeypress(moveDown, "s")
wn.onkeypress(moveLeft, "a")
wn.onkeypress(moveRight, "d")

segments = []

def reset():
    global score, segment, delay
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)

    segments.clear()

    score = 0
    delay = 0.1

    scoreBoard.clear()
    scoreBoard.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 25, "normal"))

    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

#main game
while True:
    wn.update() 

    #game end
    if head.xcor() > 280 or head.xcor() < -300 or head.ycor() > 240 or head.ycor() < -240:
        time.sleep(1)
        wn.clear()
        wn.bgcolor("red")
        scoreBoard.goto(0, 0)
        scoreBoard.write("GAME OVER ! \nCUPU BANGET >< \n\nYOUR SCORE: {} \nHIGH SCORE: {}".format(score, high_score), align="center", font=("Courier", 30, "bold"))

    #check collision with food
    if head.distance(food) < 20:
        score += 10
        if score > high_score:
            high_score = score

        scoreBoard.clear()
        scoreBoard.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 25, "normal"))

        #food location
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        food.color(random.choice(['red', 'blue', 'green', 'yellow', 'purple']))
        food.shape(random.choice(['square', 'triangle', 'circle']))
        food.speed(0)
        food.shape(food_shape)
        food.color(food_colors)
        food.goto(x, y)

        #add segment
        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape("circle")
        newSegment.color("grey")
        newSegment.penup()
        segments.append(newSegment)

    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    #check collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            wn.clear()
            wn.bgcolor("red")
            scoreBoard.goto(0, 0)
            scoreBoard.write("GAME OVER! \nCUPU BANGET >< \n\nYOUR SCORE: {} \nHIGH SCORE: {}".format(score, high_score), align="center", font=("Courier", 30, "bold"))

    time.sleep(delay)
turtle.Terminator()

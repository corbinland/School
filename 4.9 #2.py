import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightgreen")

# Set up the turtle
pen = turtle.Turtle()
pen.color("hotpink")
pen.pensize(4)
pen.speed(0)

# Function to draw a square centered at (0,0)
def draw_centered_square(size):
    pen.penup()
    pen.goto(-size/2, -size/2)  # move to bottom-left corner
    pen.pendown()
    for _ in range(4):
        pen.forward(size)
        pen.left(90)

# Draw concentric centered squares
side = 40  # starting from 40 to match the image (first visible square is not tiny)
for _ in range(6):
    draw_centered_square(side)
    side += 40  # increase size by 40 (20 per side in all directions)

pen.hideturtle()
turtle.done()

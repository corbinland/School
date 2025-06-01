import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
star = turtle.Turtle()
star.color("black")
star.pensize(2)
star.speed(2)

# Draw a 5-pointed star
for i in range(5):
    star.forward(100)
    star.right(144)

# Hide the turtle and finish
star.hideturtle()
turtle.done()


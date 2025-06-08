import turtle

# Function to draw a bar with a specific color
def draw_bar(t, height):
    # Set fill color based on height
    if height >= 200:
        t.fillcolor("red")
    elif 100 <= height < 200:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")

    # Start filling the shape
    t.begin_fill()

    # Draw the bar
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)  # Width of the bar
    t.right(90)
    t.forward(height)
    t.left(90)

    # Stop filling the shape
    t.end_fill()

    # Move to the next bar position
    t.forward(10)  # Space between bars

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")

alex = turtle.Turtle()
alex.speed(3)

# Use the given dataset for the bar chart
xs = [48, 117, 200, 240, 160, 260, 220]

# Draw bars for each value in xs
for value in xs:
    draw_bar(alex, value)

# Close the turtle graphics window on click
screen.exitonclick()

import turtle

# Scaling factor to make the square visible
scale = 50

# Set up screen
screen = turtle.Screen()
screen.title("Square with Specific Coordinates")
screen.bgcolor("white")

# Draw coordinate axes
axis = turtle.Turtle()
axis.speed(0)
axis.color("gray")

# X-axis
axis.penup()
axis.goto(-300, 0)
axis.pendown()
axis.goto(300, 0)

# Y-axis
axis.penup()
axis.goto(0, -300)
axis.pendown()
axis.goto(0, 300)

axis.hideturtle()

# Draw the square
square = turtle.Turtle()
square.color("blue")
square.pensize(2)
square.penup()

# Move to the first point (0, 0)
square.goto(0 * scale, 0 * scale)
square.pendown()

# Draw lines between the given coordinates
points = [(0, 5), (5, 5), (5, 0), (0, 0)]

for x, y in points:
    square.goto(x * scale, y * scale)

# Done
turtle.done()

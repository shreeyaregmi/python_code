import turtle

# Recursive function to draw the tree
def draw_tree(branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth == 0 or branch_length < 1:
        return

    turtle.forward(branch_length)
    
    # Draw left branch
    turtle.left(left_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    turtle.right(left_angle)

    # Draw right branch
    turtle.right(right_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    turtle.left(right_angle)

    turtle.backward(branch_length)

# Get user inputs
left_angle = float(input("Enter the left branch angle (degrees): "))
right_angle = float(input("Enter the right branch angle (degrees): "))
start_length = float(input("Enter the starting branch length (pixels): "))
reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))
depth = int(input("Enter the recursion depth: "))

# Setup turtle screen
screen = turtle.Screen()
screen.bgcolor("white")  # Set background color to white

# Setup turtle
turtle.color("black")  # Set branch color
turtle.speed("fastest")
turtle.left(90)  # Start facing up
turtle.penup()
turtle.goto(0, -250)  # Start at the bottom of the screen
turtle.pendown()

# Draw the tree
draw_tree(start_length, left_angle, right_angle, depth, reduction_factor)

# Finish
turtle.hideturtle()
turtle.done()

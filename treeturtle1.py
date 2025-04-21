import turtle

def draw_tree(branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth == 0:
        return
    
    # Change color based on depth (brown for branches, green for leaves)
    if depth > 2:
        turtle.pencolor("brown")
    else:
        turtle.pencolor("green")
    
    # Adjust thickness based on depth
    turtle.pensize(depth)
    
    # Draw the main branch
    turtle.forward(branch_length)
    
    # Draw the left subtree
    turtle.left(left_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    
    # Return to the main branch
    turtle.right(left_angle + right_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    
    # Return to the original position
    turtle.left(right_angle)
    turtle.backward(branch_length)

# Get user input
left_angle = int(input("Enter left branch angle: "))
right_angle = int(input("Enter right branch angle: "))
branch_length = int(input("Enter starting branch length: "))
depth = int(input("Enter recursion depth: "))
reduction_factor = float(input("Enter branch length reduction factor: "))

# Set up turtle
turtle.speed('fastest')
 # Set background color
turtle.left(90)  # Point upwards
turtle.up()
turtle.goto(0, -250)
turtle.down()

# Draw tree
draw_tree(branch_length, left_angle, right_angle, depth, reduction_factor)
turtle.hideturtle()
turtle.done()

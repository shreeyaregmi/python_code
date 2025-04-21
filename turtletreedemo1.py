import turtle
from turtle import *

# Set up the turtle
shape("turtle")
speed("fastest")
left(90)  # Start facing upward

# Recursive tree function
def draw_tree(branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth == 0:
        return
    forward(branch_length)
    
    # Left branch
    left(left_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    
    # Right branch
    right(left_angle + right_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    
    # Return to previous state
    left(right_angle)
    backward(branch_length)

# User input
LEFT_ANGLE = float(input("Enter left branch angle (e.g., 20): "))
RIGHT_ANGLE = float(input("Enter right branch angle (e.g., 25): "))
START_LENGTH = float(input("Enter starting branch length (e.g., 100): "))
RECURSION_DEPTH = int(input("Enter recursion depth (e.g., 5): "))
REDUCTION = float(input("Enter branch length reduction factor (e.g., 0.7): "))

# Move turtle to starting position
penup()
goto(0, -250)
pendown()

# Draw the tree
draw_tree(START_LENGTH, LEFT_ANGLE, RIGHT_ANGLE, RECURSION_DEPTH, REDUCTION)

# Finish
turtle.done()

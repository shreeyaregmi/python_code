import turtle as trl
screen = trl.Screen()
t = trl.Turtle()



start_x = -50
start_y = -50
end_x = 50
end_y = 50


t.penup()
t.goto(start_x, start_y)
t.pendown()
t.goto(end_x, end_y)

t.hideturtle()
trl.done()
import turtle as trl 

trl.shape("turtle")


def draw_shape(shape, color):
    trl.color(color)
    
    if shape == "square":
        for i in range(0,4):
            trl.fd(50)
            trl.lt(90)
        trl.fd(75)
    if shape == "triangle":
        for i in range(0,3):
            trl.fd(50)
            trl.lt(120)
        trl.fd(75)

draw_shape("square", "red")
draw_shape("triangle", (1,0,0))
draw_shape("square", "green")
draw_shape("triangle", "purple")


delay = input("press enter")

import turtle as trl 
trl.shape("turtle")
def draw_square():
    for i in range(0,4):
        trl.fd(50)
        trl.lt(90)
    trl.fd(75)
    
def draw_triangle():
    for i in range(0,3):
        trl.fd(50)
        trl.lt(120)
    trl.fd(75)

draw_square()
draw_triangle()
draw_square()
draw_triangle()


delay = input("press enter")

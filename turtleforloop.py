
import turtle



def draw_a_star():
    star = turtle.Turtle()

    for i in range(5):
        star.forward(50)
        star.right(144)
        
    turtle.done()

def draw_a_box():
    box=turtle.Turtle()
    box.setx(-200)
    box.sety(200)
    for i in range(4):
        print(box.pos())
        box.forward(200)
        box.right(90)
    turtle.done()



#draw_a_star()
draw_a_box()

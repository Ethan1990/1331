import turtle 

rat = turtle.Turtle()

dot_distance = 50
width = 5
height = 1

rat.penup()

def draw_octogon():
    rat.pd()
    num_sides = 6
    side_length = 20
    angle = 360.0 / num_sides 

    for i in range(num_sides):
        rat.forward(side_length)
        rat.right(angle)
    rat.pu()



def draw_a_grid():

    for y in range(height):
        for i in range(width):
            draw_octogon()
            rat.forward(dot_distance)
        rat.backward(dot_distance * width)
        rat.right(90)
        rat.forward(dot_distance)
        rat.left(90)
    
draw_octogon()
rat.forward(dot_distance)
rat.left(30)
draw_octogon()
rat.forward(dot_distance)
rat.left(30)
draw_octogon()
rat.forward(dot_distance)
rat.left(30)
draw_octogon()
rat.forward(dot_distance)
rat.left(30)
draw_octogon()

turtle.done()

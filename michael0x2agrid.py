import turtle, random

rat = turtle.Turtle()
screen = turtle.Screen()
dot_distance = 75
#width = 5
height = 5

rat.penup()
screen.register_shape("NickCage.gif")
rat.shape("NickCage.gif")
def draw_a_star():
    
    for i in range(5):
        rat.pendown()
        rat.forward(50)
        rat.right(144)
        rat.penup()
        


for y in range(height):
#    rat.dot()
    rat.right(random.randrange(0,360,1))
    rat.forward(dot_distance-random.randrange(-100,100,1))
    draw_a_star()
    
turtle.done()

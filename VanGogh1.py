import turtle, random
 
vangogh = turtle.Turtle()
 
dot_distance = 25
width = 5
height = 7
screen=vangogh.screen
screen.title("Happy Trees")
vangogh.pu()
#print(screen.screensize())
screen.bgcolor("lightblue")

#cloud="C:\\Users\\newsomc\\Desktop\\1331Newsom\\raincloud.gif"

#cloud="raincloud.gif"
cloud="si_logo2.gif"
#mrcloud.turtlesize(0.5,0.5)    #takes positive integers

vg=vangogh
vg.speed(10)    # 10 is fastest, I think.
vg.width(3)     # default is 1px

def tree(branchLen,t):
    t.pencolor("brown")
    t.fillcolor("green")

    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.stamp()
        t.backward(branchLen)


def drawForest(t):
    """Draw 5 trees in random locations
    within the grassy area."""

    #tree(75,vg)
    t.pu()
    ss=screen.screensize()
    t.setx(random.randrange(0,ss[0],1)-ss[0]/2)
    t.sety(random.randrange(0,ss[1],1)-ss[1]/2 -300)
    t.pd()
    tree(random.randrange(50,80,1),t)
    print(t.position())

    
def drawsun(t):
    """Draws a sun like shape."""
    t.pu()
    st=20
    t.setx(200)
    t.sety(200)
    t.pd()
    t.begin_fill()
    t.pencolor("orange")
    t.fillcolor("yellow")
    for i in range(0,360, st ):

        t.left(70)
        t.forward(10)
        t.right(150)
        t.forward(10)
        t.left(80-st)
    t.end_fill()



def drawgrass(t):
    t.pu()
    t.setx((screen.screensize()[0])*-1)
#    vg.setx(-120)
    t.sety(-100)
    t.pd()
    t.begin_fill()     
    t.pencolor("green")
    t.fillcolor("lightgreen")

     
    #for item in range(screen.canvwidth):
    while t.xcor() < 400:
#    for item in range(240):
        t.right(random.randrange(0,3,1)-1)
        t.forward(12)
#        vg.left(random.randrange(-1,1,1))
    t.seth(-90)
    while t.ycor() > -100:
        t.forward(10)

    t.forward(300)
    t.right(90)
    t.forward(screen.canvwidth*2)
    t.right(90)
    while t.ycor() < -100:
        t.forward(10)
    t.end_fill()

def drawgrass2(t):
    t.pu()
    t.setx((screen.screensize()[0])*-1)
#    vg.setx(-120)
    t.sety(-300)
    t.pd()
##    t.begin_fill()     
    t.pencolor("lightgreen")
##    t.fillcolor("lightgreen")
    t.pensize(300)

     
    #for item in range(screen.canvwidth):
    while t.xcor() < 400:
#    for item in range(240):
        t.right(random.randrange(0,3,1)-1)
        t.forward(12)
#        vg.left(random.randrange(-1,1,1))
    t.pensize(3)

def goHome(t):
    """Move the turtle to 0,0."""
    t.pu()
    t.setx(0)
    t.sety(0)
    t.pd()
    

        

def drawcloud(t):
    """ Draws a cloud"""
    t.pu()
    st=1
    t.setx(-400)
    t.sety(200)
    #t.pd()
    t.st()
#    vg.begin_fill()
#    vg.pencolor("orange")
#    vg.fillcolor("yellow")
    t.speed(2)
    for i in range(0,1000, st ):
        t.forward(1)
##
##        vg.left(70)
##        vg.forward(10)
##        vg.right(150)
##        vg.forward(10)
##        vg.left(80-st)
#    vg.end_fill()


#drawCoordSystem3()
# The main program
drawgrass2(vg)
drawsun(vg)
#for i in range(3):
#    drawForest(vg)
screen.register_shape(cloud)
#rat.shape("NickCage.gif")
mrcloud=turtle.Turtle()
mrcloud.ht()
mrcloud.shape(cloud)

drawcloud(mrcloud)
   
turtle.done()

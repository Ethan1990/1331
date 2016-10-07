import turtle

side_length = 300
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()       # Create alex
alex.color("blue")
alex.pensize(5)
alex.shape("turtle")

tess.forward(side_length)             # Make tess draw equilateral triangle
tess.left(120)
tess.forward(side_length)
tess.left(120)
tess.forward(side_length)
tess.left(120)               # Complete the triangle

tess.right(180)              # Turn tess around
tess.forward(80)             # Move her away from the origin


alex.forward(side_length)             # Make alex draw a square
alex.left(90)
alex.forward(side_length)
alex.left(90)
alex.forward(side_length)
alex.left(90)
alex.forward(side_length)
alex.left(90)

wn.mainloop()

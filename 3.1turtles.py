

import turtle, time             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
time.sleep(1)
alex = turtle.Turtle()    # Create a turtle, assign to alex
time.sleep(1)
alex.forward(50)          # Tell alex to move forward by 50 units
time.sleep(1)
alex.left(90)           # Tell alex to turn by 90 degrees
time.sleep(1)
alex.forward(30)          # Complete the second side of a rectangle
time.sleep(1)
wn.mainloop()             # Wait for user to close window

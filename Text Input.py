from graphics import *
import random
import math
# open a window
window = GraphWin("Radius", 400, 400)

# draw an entry
entry = Entry(Point(200, 200), 17)
entry.draw(window)

# wait for a click
while window.checkMouse( ) == None:
  pass

# read the input
radius = int(entry.getText( ))

# hide the entry
entry.undraw( )

# make the circle in the center
circle = Circle(Point(200, 200), radius)

# set the circle to a random colors
color = color_rgb(random.randint(0, 255),
                  random.randint(0, 255),
                  random.randint(0, 255))
circle.setFill(color)

# draw it
circle.draw(window)

# make text for the area at the bottom
area = math.pi * radius ** 2
text1 = Text(Point(200,350), "Area = " + str(area))
text1.setTextColor("blue")
text1.draw(window)

# make text for the circumference
circ = 2 * math.pi * radius
text2 = Text(Point(200,380), "Circumference = " + str(circ))
text2.setTextColor("yellow")
text2.draw(window)

while window.checkMouse( ) == None:
  pass

window.close( )

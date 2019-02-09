import time
from graphics import *

# create the window
window = GraphWin("Mario", 400, 400)

# set the background to white
window.setBackground("white")

# draw a "ground" rectangle
r = Rectangle(Point(0, 365), Point(400, 400))
r.setFill("darkgreen")
r.setOutline("darkgreen")
r.draw(window)

# load the images
l1 = Image(Point(0, 350), "l1.gif")
l2 = Image(Point(0, 350), "l2.gif")
r1 = Image(Point(0, 350), "r1.gif")
r2 = Image(Point(0, 350), "r2.gif")

# start going right
right = True
step = 1

# loop until the user clicks
while window.checkMouse( ) == None:
  # pick the image to show
  if right and step == 1:
    r1.draw(window)
    r2.undraw( )
    l1.undraw( )
    l2.undraw( )
  if right and step == 2:
    r2.draw(window)
    r1.undraw( )
    l1.undraw( )
    l2.undraw( )
  if not right and step == 1:
    l1.draw(window)
    r2.undraw( )
    r1.undraw( )
    l2.undraw( )
  if not right and step == 2:
    l2.draw(window)
    r2.undraw( )
    l1.undraw( )
    r1.undraw( )
  
  # update step
  if step == 1:
    step = 2
  else:
    step = 1

  # update position
  if right:
    increment = 5
  else:
    increment = -5
  l1.move(increment, 0)
  l2.move(increment, 0)
  r1.move(increment, 0)
  r2.move(increment, 0)

  # if we go too far, go in other direction!
  position = l1.getAnchor( ).getX( )
  if position < 0 or position > 400:
    right = not right

  # sleep for one quarter second
  time.sleep(0.25)



# close the window
window.close( )

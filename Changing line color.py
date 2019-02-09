import turtle 

painter = turtle.Turtle()

painter.pencolor("green")

for i in range(50):
    painter.forward(50)
    painter.left(120) # Let's go counterclockwise this time 
    
painter.pencolor("yellow")
for i in range(50):
    painter.forward(50)
    painter.left(123)
    
painter.pencolor("red")
for i in range(50):
    painter.forward(10)
    painter.left(123)

painter.pencolor("yellow")
for i in range(50):
    painter.forward(50)
    painter.left(123)

painter.pencolor("Orange")
for i in range(50):
    painter.forward(60)
    painter.left(123)

    
turtle.done()

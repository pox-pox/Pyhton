import turtle

turtle.shape('classic')

def drawRect(side):
    turtle.pendown()
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(10 + int(side))
        turtle.left(90)
        
    turtle.penup()
    turtle.goto(-side*0.5, -side*0.5)
for i in range(10,50,10):
    drawRect(i)

turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
end_fill()
done()

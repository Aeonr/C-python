import turtle

def curvemove():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color('blue')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curvemove()
turtle.left(120)
curvemove()
turtle.forward(111.65)
turtle.end_fill()

turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()
turtle.write('CYH',font = ('SimHei',15,'bold'))
turtle.hideturtle()

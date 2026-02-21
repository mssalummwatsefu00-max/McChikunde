import turtle 
import random
turtle.setup(900,900)
turtle.bgcolor("black")
turtle.speed(2)
turtle.tracer(3)
for i in range(300):
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(random.randint(0,360))
    turtle.pendown()
    turtle.pencolor(random.random(),random.random(), 1)
    turtle.forward(i*1.5)
    turtle.dot(3)
    if i % 5 == 0:
        turtle.update()
        turtle.hideturtle()
turtle.done()
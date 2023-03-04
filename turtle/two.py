import turtle
t=turtle.Turtle()
t.speed(0)
t.pensize(8)
t.penup()
t.goto(0,-100)
t.pendown()

# draw head
for i in range(36):
    t.forward(30)
    t.left(10)
# draw eyes
t.penup()
t.goto(-80,90)
t.pendown()
t.left(90)
for i in range(45):
    t.forward(2)
    t.right(4)

t.penup()
t.goto(50,90)
t.pendown()

t.left(-180)
for i in range(45):
    t.forward(2)
    t.right(4)

# draw nose
t.penup()
t.goto(0,50)



turtle.done()
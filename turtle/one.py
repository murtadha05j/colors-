import turtle

w = turtle.Turtle()
w.speed(5)





for i in range(360):
    w.fd(20)
    w.rt(90)
    if i==90:
        w.forward(34)
        w.right(13)


turtle.done()
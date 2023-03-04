# Python program to draw square 
# using Turtle Programming
import turtle

w = turtle.Turtle()
w.color('green')
w.shape('turtle')
w.speed(1020)
x=0
while x < 120: # while the value of x is lesser than 120,
                #continuously do this:
    w.fd(200)
    w.rt(61)
    w.color('red')
    w.fd(200)
    w.rt(61)
    w.color('black')
    w.fd(200)
    w.color('blue')
    w.rt(61)
    w.fd(200)
    w.rt(61)
    w.fd(200)
    w.rt(61)
    w.color('green')
    w.fd(200)
    w.rt(61)

    w.rt(11.111)
    x = x+1

turtle.done()

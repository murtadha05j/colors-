import turtle

# --- Setup ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Butterfly Effect - Lorenz Attractor")
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.colormode(255)

# Lorenz system parameters
sigma = 10
rho = 28
beta = 8/3

# Initial values
x, y, z = 0., 1., 1.05
dt = 0.01

points = []

# Generate points
for i in range(8000):
    dx = sigma * (y - x) * dt
    dy = (x * (rho - z) - y) * dt
    dz = (x * y - beta * z) * dt
    x += dx
    y += dy
    z += dz
    points.append((x, y, z))

# Scale for screen
scale = 8

# Draw attractor
for i, (x, y, z) in enumerate(points):
    r = (i * 5) % 255
    g = (i * 2) % 255
    b = (i * 7) % 255
    t.color(r, g, b)
    t.penup()
    t.goto(x * scale, y * scale)
    t.pendown()
    t.dot(2)

turtle.done()

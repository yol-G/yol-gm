import turtle
import random

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Gambar Abstrak Estetik")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Fungsi buat lingkaran berwarna acak
def draw_colored_circle(x, y, radius):
    t.up()
    t.goto(x, y - radius)
    t.down()
    t.color(random.random(), random.random(), random.random())
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Fungsi buat garis abstrak
def draw_random_line():
    t.up()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.down()
    t.pencolor(random.random(), random.random(), random.random())
    t.width(random.randint(1, 4))
    t.forward(random.randint(50, 200))

# Fungsi buat spiral abstrak
def draw_spiral(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.pencolor(random.random(), random.random(), random.random())
    for i in range(30):
        t.forward(i * 3)
        t.right(30)

# Buat pola lingkaran
for _ in range(15):
    draw_colored_circle(random.randint(-250, 250), random.randint(-200, 200), random.randint(10, 50))

# Buat pola garis
for _ in range(20):
    draw_random_line()

# Buat beberapa spiral
for _ in range(5):
    draw_spiral(random.randint(-200, 200), random.randint(-150, 150))

turtle.done()

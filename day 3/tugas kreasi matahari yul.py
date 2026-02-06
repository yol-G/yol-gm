import turtle
import random

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Gambar Abstrak")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Fungsi membuat lingkaran dengan warna acak
def draw_colored_circle(x, y, radius):
    t.up()
    t.goto(x, y - radius)  # titik tengah lingkaran
    t.down()
    t.color(random.random(), random.random(), random.random())
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Fungsi membuat garis acak
def draw_random_line():
    t.up()
    t.goto(random.randint(-300, 300), random.randint(-200, 200))
    t.down()
    t.pencolor(random.random(), random.random(), random.random())
    t.forward(random.randint(50, 200))

# Buat beberapa lingkaran dan garis
for _ in range(10):
    draw_colored_circle(random.randint(-200, 200), random.randint(-150, 150), random.randint(20, 60))

for _ in range(20):
    draw_random_line()

turtle.done()

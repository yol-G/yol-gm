import turtle
import random

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Abstrak Biru Blur + Pasir Abu")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.colormode(255)  # supaya bisa pakai RGB

# Fungsi buat lingkaran biru blur
def draw_blue_blur(x, y, radius):
    t.up()
    t.goto(x, y - radius)
    t.down()
    # variasi biru blur
    r = random.randint(0, 100)
    g = random.randint(0, 100)
    b = random.randint(150, 255)
    t.color((r, g, b))
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Fungsi buat efek pasir abu-abu
def draw_sand(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    shade = random.randint(100, 200)
    t.dot(random.randint(2,5), (shade, shade, shade))  # dot kecil untuk efek pasir

# Buat banyak lingkaran biru blur
for _ in range(25):
    draw_blue_blur(random.randint(-300, 300), random.randint(-250, 250), random.randint(20, 70))

# Tambahkan efek pasir abu
for _ in range(150):
    draw_sand(random.randint(-350, 350), random.randint(-300, 300))

# Tambahkan beberapa garis tipis putih untuk efek highlight
for _ in range(20):
    t.up()
    t.goto(random.randint(-300,300), random.randint(-250,250))
    t.down()
    t.pencolor(255, 255, 255)
    t.width(random.randint(1,2))
    t.forward(random.randint(30, 100))

turtle.done()

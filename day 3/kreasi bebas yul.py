import turtle
import random

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Abstrak Merah-Putih-Biru-Kuning")
turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Fungsi blur lingkaran dengan variasi warna
def draw_blur_circle(x, y, radius, color):
    t.up()
    t.goto(x, y - radius)
    t.down()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Layer utama merah blur di tengah
for i in range(5):
    r = 255
    g = random.randint(0, 80)
    b = random.randint(0, 80)
    draw_blur_circle(0, 0, 50 + i*15, (r, g, b))

# Putih blur mengelilingi merah
for i in range(4):
    shade = random.randint(200, 255)
    draw_blur_circle(0, 0, 120 + i*15, (shade, shade, shade))

# Biru gelap blur di background
for i in range(10):
    draw_blur_circle(random.randint(-250,250), random.randint(-200,200), random.randint(30,70),
                     (random.randint(0,20), random.randint(0,20), random.randint(100,200)))

# Kuning sebagai highlight titik kecil
for _ in range(40):
    x = random.randint(-300,300)
    y = random.randint(-250,250)
    t.up()
    t.goto(x, y)
    t.down()
    t.dot(random.randint(3,8), (255, 255, 0))

turtle.done()

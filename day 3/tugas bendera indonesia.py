import turtle

# Setup layar
screen = turtle.Screen()
screen.title("Bendera Indonesia Terbalik")
screen.setup(width=800, height=500)
screen.bgcolor("lightgray")  # biar putih kelihatan jelas

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Fungsi gambar persegi panjang
def draw_rectangle(x, y, width, height, color):
    t.up()
    t.goto(x, y)
    t.down()
    t.color("black", color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Ukuran bendera
flag_width = 600
flag_height = 300
start_x = -300
start_y = 150

# Bagian putih (atas)
draw_rectangle(start_x, start_y, flag_width, flag_height / 2, "white")

# Bagian merah (bawah)
draw_rectangle(start_x, start_y - flag_height / 2, flag_width, flag_height / 2, "red")

# Opsional: tiang bendera
t.up()
t.goto(start_x - 20, start_y + 50)
t.down()
t.pensize(5)
t.color("black")
t.right(90)
t.forward(flag_height + 100)

turtle.done()

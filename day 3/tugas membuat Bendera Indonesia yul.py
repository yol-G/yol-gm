import turtle

screen = turtle.Screen()
screen.title("Bendera Indonesia")
screen.bgcolor("lightgray")  # background diubah
screen.setup(width=800, height=500)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_rectangle(x, y, width, height, color):
    t.up()
    t.goto(x, y)
    t.down()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

flag_width = 600
flag_height = 300
start_x = -300
start_y = 150

# Merah (atas)
draw_rectangle(start_x, start_y, flag_width, flag_height / 2, "red")

# Putih (bawah)
draw_rectangle(start_x, start_y - flag_height / 2, flag_width, flag_height / 2, "white")

turtle.done()

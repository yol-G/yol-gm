import turtle

t = turtle.Turtle()
t.speed(3)
t.hideturtle()

# Badan rumah
t.up()
t.goto(-75, -75)
t.down()
t.color("black", "orange")
t.begin_fill()
for _ in range(4):
    t.forward(150)
    t.left(90)
t.end_fill()

# Atap rumah (segitiga)
t.up()
t.goto(-75, 75)
t.down()
t.color("black", "red")
t.begin_fill()
t.goto(0, 150)     # puncak atap
t.goto(75, 75)     # sisi kanan atap
t.goto(-75, 75)    # kembali ke kiri
t.end_fill()

turtle.done()


# SeychellesFlag.py
import turtle

def drawRectangle(ttl, x, y, width, height):
    """Draw a rectangle of dimensions width and height, with upper
       left corner at x,y"""
    ttl.up()
    ttl.goto(x, y)
    ttl.setheading (0)
    ttl.down()
    for i in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.up()

def drawTriangle(ttl, x1, y1, x2, y2, x3, y3):
    ttl.up()
    ttl.goto(x1, y1)
    ttl.down()
    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x1, y1)

def fillTriangle(ttl, x1, y1, x2, y2, x3, y3, color):
    """Fill triangle of color = string value"""
    ttl.fillcolor(color)
    ttl.begin_fill()
    drawTriangle(ttl, x1, y1, x2, y2, x3, y3)
    ttl.end_fill()

# set the screen size in pixels = 1000 x 1000
turtle.setup(1200, 1000, 0, 0)
myrtle = turtle.Turtle()
myYellow = "#FFD700"
myRed = "#D4213D"
myWhite = "#FFFFFF"
myBlue = "#003F87"
myGreen = "#007A3D"

# Use a turtle to draw
Joe = turtle.Turtle()
Joe.screen.colormode(255)
Joe.speed(0)
drawRectangle(Joe, -600, 500, 800, 300)

# Draw blue triangle
fillTriangle(Joe, 0, 0, -600, 500, 200, 500, myBlue)

# Draw yellow triangle
fillTriangle(Joe, 0, 0, -600, 300, 200, 300, myYellow)

# Draw red triangle
fillTriangle(Joe, 0, 0, -600, 200, 200, 200, myRed)

# Draw white triangle
fillTriangle(Joe, 0, 0, -600, 100, 200, 100, myWhite)

# Draw green triangle
fillTriangle(Joe, 0, 0, -600, 50, 200, 50, myGreen)

Joe.hideturtle()

# to create a postscript imagefile
ts = turtle.getscreen()
ts.postscript(file="SeychellesFlag.eps")

turtle . done ()# convert to jpeg
# save_as_jpg("SeychellesFlag")

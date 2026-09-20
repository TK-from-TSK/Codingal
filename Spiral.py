import turtle 
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Spiral")

my_pen = turtle.Turtle()

size = 0
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

while True:
    for i in range(4):
        my_pen.pencolor(colors[i])
        my_pen.fd(size + 1)
        my_pen.left(90)
        size = size-5

    size = size + 1

import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("blue")
my_wn.setup(300,400)

my_turtle = turtle.Turtle()
size = 0

while True:
    for i in range(4):
        my_turtle.forward(size)
        my_turtle.left(90)
    size = size - 5
    size = size + 1

turtle.done()
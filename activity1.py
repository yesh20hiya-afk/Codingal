import turtle

turtle.Screen().bgcolor("green")
turtle.Screen().setup(300,400)

Polygon = turtle.Turtle()
num_of_sides = 6
side_length = 70
angle = 360/num_of_sides
for i in range(num_of_sides):
    Polygon.forward(side_length)
    Polygon.right(angle)

turtle.done()
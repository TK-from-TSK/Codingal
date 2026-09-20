import turtle as t
t.Screen().bgcolor("Red")
t.Screen().setup(300, 400)


num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    t.forward(side_length)
    t.right(angle)

t.done()
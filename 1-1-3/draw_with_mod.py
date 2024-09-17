import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 20

# iterate
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    # Chanigng the program to modify the color every three floors

    if floor % 6 == 0:
     painter.color("gray")

    if floor % 6 == 3:

        painter.color("blue")
y = y + 10  # location of next floor

rem = floor % 6
if (rem > 2):
  painter.color("blue")
# draw the floor
painter.pendown()
painter.forward(50)
wn = trtl.Screen()
wn.mainloop()












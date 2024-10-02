#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
body = trtl.Turtle()
body.pensize(40)
body.circle(20)
Legs = 8
length = 70
z = 380 / Legs
body.pensize(5)
n = 0
while (n < Legs):
  body.goto(0,0)
  body.setheading(z*n)
  body.forward(length)
  n = n + 1
  body.hideturtle()













wn = trtl.Screen()
wn.mainloop()


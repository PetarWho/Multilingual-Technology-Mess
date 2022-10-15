from turtle import *

Screen().setup(width=1.0, height=1.0, startx=None, starty=None)
Screen().bgcolor("black")
speed(3)

penup()
pensize(15)
pencolor("orange")
goto(-300, 140)

# I upper
pendown()
forward(100)

penup()
goto(-250, 140)
right(90)

# I line
pendown()
forward(160)

penup()
goto(-300, -20)

# I down
pendown()
left(90)
forward(100)

penup()

# Heart
goto(0, -40)
pendown()
color("red")
begin_fill()
pensize(20)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

# U

penup()
pensize(15)
pencolor("orange")
goto(200, 140)
right(40)

pendown()
forward(110)
circle(60, 180)
forward(110)

# UNDERLINE

penup()
pensize(10)
speed(6)
pencolor("cyan")
goto(-360, -100)
right(90)

pendown()
forward(730)

done()

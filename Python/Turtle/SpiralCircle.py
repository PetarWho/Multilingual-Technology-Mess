from turtle import *

Screen().bgcolor('black')
pensize(2)
speed(1000)

# Iterate six times in total
for i in range(6):

    # Choose your color combination
    for color1 in ('red', 'magenta', 'blue',
                  'cyan', 'green', 'white',
                  'yellow'):
        color(color1)

        # Draw a circle of chosen size, 100 here
        circle(100)

        # Move 10 pixels left to draw another circle
        left(10)

    # Hide the cursor(or turtle) which drew the circle
    hideturtle()
done()

import pgzrun

WIDTH = 500
HEIGHT = 500

Title = "Color Changing Circles"

circles = ["redcircle,bluecircle,greencircle"]
x = 0
y = 0

current = 0
circle = Actor(circles[current])
circle.pos(x,y)
def draw():
    screen.clear()
    screen.fill("white")
    circle.draw()



pgzrun.go()
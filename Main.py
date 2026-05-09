import pgzrun

WIDTH = 500
HEIGHT = 500

TITLE = "Color Changing Circles"

circles = ["redcircle", "bluecircle","greencircle"]
x = 250
y = 250

current = 0
circle = Actor(circles[current])
circle.pos = (x,y)
def draw():
    screen.clear()
    screen.fill("white")
    circle.draw()

def on_mouse_down(pos):
    global current 
    circle.pos = pos
    current += 1 # shorter way of current = current + 1 
    if current >= len(circles):
        current = 0 
    circle.image = circles[current]

pgzrun.go()
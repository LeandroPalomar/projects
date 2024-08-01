WIDTH = 1252
HEIGHT = 700

mushroom = Actor('mushroom.png')
mushroom.pos = WIDTH/2, HEIGHT/2

def draw():
    screen.fill((0, 230, 7))
    mushroom.draw()

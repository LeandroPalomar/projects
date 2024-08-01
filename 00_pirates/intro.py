import numpy as np
import random
import pygame
import sys

WIDTH = 1792  # Bredde
HEIGHT = 1024  # Høyde

from objects import Coin
from objects import Sword
from objects import Diamond
from objects import Bomb
from objects import Pirate
from objects import Crosshair

pygame.mouse.set_visible(False)
TITLE = "LEO PIRATAS"

gravity = 3

background = Actor("background_alpha.png")

caravel = Actor("caravel_128.png")
caravel.pos = (64, 960)
caravel.width = 128
caravel.height = 128

crosshair = Actor("crosshair_64.png")
crosshair.pos = (WIDTH/2.0, HEIGHT/2.0)
crosshair.width = 64
crosshair.height = 64

music.play("8-bit-game-158815.ogg")

objects = list()
objects.append(Coin())
score = 0
frame = 0

def on_mouse_move(pos):
    crosshair.pos = pos

def on_mouse_down(pos):
    global objects
    for object in objects:
        if is_collision(crosshair,object):
            objects.remove(object)


def update():

    global score
    global frame

    if keyboard.right:
        if caravel.x > WIDTH - caravel.width / 2.0:
            pass
        else:
            caravel.x += 10

    if keyboard.left:
        if caravel.x < caravel.width / 2.0:
            pass
        else:
            caravel.x -= 10

    for object in objects:
        if object is not None:
            object.y += gravity
            if is_collision(caravel, object):
                objects.remove(object)
                if hasattr(object, 'score'):
                    score+=object.score
                else:
                    score = 0
            elif object.y > HEIGHT:
                objects.remove(object)

    if should_generate_object(Coin.probability-frame*0.0000001):
        newcoin = Coin()
        newcoin.pos = (random.randint(0+newcoin.width/2.0,WIDTH-newcoin.width/2.0), 0 + newcoin.width / 2.0)
        objects.append(newcoin)

    if should_generate_object(Sword.probability+frame*0.0000001):
        newsword = Sword()
        newsword.pos = (random.randint(0+newsword.width/2.0,WIDTH-newsword.width/2.0), 0 + newsword.width / 2.0)
        objects.append(newsword)

    if should_generate_object(Diamond.probability-frame*0.0000001):
        newdiamond = Diamond()
        newdiamond.pos = (random.randint(0+newdiamond.width/2.0,WIDTH-newdiamond.width/2.0), 0 + newdiamond.width / 2.0)
        objects.append(newdiamond)

    if should_generate_object(Bomb.probability+frame*0.0000001):
        newbomb = Bomb()
        newbomb.pos = (random.randint(0+newbomb.width/2.0,WIDTH-newbomb.width/2.0), 0 + newbomb.width / 2.0)
        objects.append(newbomb)

    if should_generate_object(Pirate.probability+frame*0.0000001):
        newpirate = Pirate()
        newpirate.pos = (random.randint(0+newpirate.width/2.0,WIDTH-newpirate.width/2.0), 0 + newpirate.width / 2.0)
        objects.append(newpirate)

    frame += 1

def draw():
    global score
    screen.clear()
    background.draw()
    caravel.draw()
    for object in objects:
        if object is not None:
            object.draw()

    crosshair.draw()

    screen.draw.text(f"Score: {score}", (50, 30), color="Black")

def is_collision(obj1, obj2):
    # Check if there is no collision
    if (
        obj1.x > obj2.x + obj2.width
        or obj1.x + obj1.width < obj2.x
        or obj1.y > obj2.y + obj2.height
        or obj1.y + obj1.height < obj2.y
    ):
        return False
    # If none of the above, there is a collision
    return True

def should_generate_object(probability):
    """
    Determines if an event should occur based on a given probability.

    :param probability: Probability of event occurring (between 0 and 1).
    :return: True if event should occur, False otherwise.
    """
    return random.random() < probability

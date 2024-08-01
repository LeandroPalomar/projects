from pgzero.actor import Actor

class Coin(Actor):

    fileName = 'coin_64.png'
    width = 64
    height = 64
    probability = 0.01

    def __init__(self):
        Actor.__init__(self, Coin.fileName)
        self.score = 1


class Sword(Actor):

    fileName = 'sword_64.png'
    width = 64
    height = 64
    probability = 0.01

    def __init__(self):
        Actor.__init__(self,Sword.fileName)
        self.score = -1

class Diamond(Actor):

    fileName = 'diamond_64.png'
    width = 64
    height = 64
    probability = 0.005

    def __init__(self):
        Actor.__init__(self,Diamond.fileName)
        self.score = 10


class Bomb(Actor):

    fileName = 'bomb_64.png'
    width = 64
    height = 64
    probability = 0.005

    def __init__(self):
        Actor.__init__(self,Bomb.fileName)
        self.score = -10


class Pirate(Actor):

    fileName = 'pirate_64.png'
    width = 64
    height = 64
    probability = 0.005

    def __init__(self):
        Actor.__init__(self,Pirate.fileName)

class Crosshair(Actor):

    fileName = 'crosshair_64.png'
    width = 64
    height = 64

    def __init__(self):
        Actor.__init__(self,Crosshair.fileName)

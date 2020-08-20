import pygame
from player import Player     # depuis le fichier player importe la classe Player


# create a second class for the game
class Game:

    def __init__(self):
        # generate our player for new party
        self.player = Player()
        self.pressed = {}


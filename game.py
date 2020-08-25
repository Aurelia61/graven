import pygame
from player import Player     # depuis le fichier player importe la classe Player
from monster import Monster


# create a second class for the game
class Game:

    def __init__(self):
        # generate our player for new party
        self.player = Player()
        # group of monster
        self.all_monsters = pygame.sprite.Group()      # crée un groupe de monstres
        self.pressed = {}
        self.spawn_monster()     # générer un premier exemplaire au démarrage du jeu


    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)     # ajouter un monster au groupe de monstres



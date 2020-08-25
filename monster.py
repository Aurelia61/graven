# coding : utf-8

import pygame

# create a class monster

class Monster(pygame.sprite.Sprite):      # la classe Monster hérite de la super classe Sprite qui est pour les éléments graphiques du jeu

    def __init__(self):
        super().__init__()
        self.health = 100          # point(s) de vie actuel(s)
        self.max_health = 100      # points de vie max
        self.attack = 5            # points d'attaque infligés au joueur
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()     # récupère le "rectangle" de l'image comme dimensions
        self.rect.x = 1000    # image le plus à droite possible !! récupérer la position au lieu de coder en dur le chiffre !!



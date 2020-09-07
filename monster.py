# coding : utf-8

import pygame
import random

# create a class monster

class Monster(pygame.sprite.Sprite):      # la classe Monster hérite de la super classe Sprite qui est pour les éléments graphiques du jeu

    def __init__(self, game):
        super().__init__()         # appel de la super classe
        self.game = game
        self.health = 100          # point(s) de vie actuel(s)
        self.max_health = 100      # points de vie max
        self.attack = 5            # points d'attaque infligés au joueur
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()     # récupère le "rectangle" de l'image comme dimension
        self.rect.x = 1000 + random.randint(0, 300)   # image le plus à droite possible + un chiffre aléatoire pour que les monstres n'apparaissent pas au même endroit (!! récupérer la position au lieu de coder en dur le chiffre !!)
        self.rect.y = 540
        self.velocity = 2   # vitesse de déplacement du monstre

    def damage(self, amount):    # amount, c'est le montant de point de vie perdu
        # inflict the damage
        self.health -= amount
        
        # check if the new number of life point is lower or nul 
        if self.health <= 0 :
            # re-emerge like a new monster  (not delete in the purpose of saving place)
            # put the monster at the beginning place
            self.rect.x = 1000
            # put he health point at the max
            self.health = self.max_health




    def update_health_bar(self, surface):   # surface = l'endroit où^on va placer la jauge
        # define a color for the life bar (green)
        bar_color = (111, 210, 46)

        # define a color for the background of the bar (grey)
        back_bar_color = (60, 63, 60)

        # define the position (X, Y) of the life bar, also the Weight (depend on life point) and the Height 
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]    # [X, Y, W, H] H = hauteur de la jauge en pixel
        
        # definir the position of the background of the life bar
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # draw our life bar
        pygame.draw.rect(surface, back_bar_color, back_bar_position)    # mettre la jauge qui fait la longueur max (le fond gris) avant la jauge de vie pour que cette dernière soit visible
        pygame.draw.rect(surface, bar_color, bar_position)   # créer un rectangle sur la surface qu'on a récupérer avec une certaine couleur et à une certaine position


    def forward(self):
        # movement only if there isn't a collision with the groupe de player
        if not self.game.check_collision(self, self.game.all_players) :   # le premier self correspond au monster
            self.rect.x -= self.velocity    # récupérer les coordonnées du monstre et faire déplacer le monstre vers le joueur, donc "-"





import pygame

# create the first class for the player
class Player(pygame.sprite.Sprite):    # sprite pour charger le joueur

    def __init__(self) :
        super().__init__()   # appel de la super class
        self.health = 100
        self.max_health = 100
        self.attack = 10     # point d'attaque / degats faits par le joueur
        self.velocity = 5    # vitesse du joueur
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()  # récupère un rectangle
        self.rect.x = 400     # en partant de gauche
        self.rect.y = 500     # en partant du haut
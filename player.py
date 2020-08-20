import pygame
from projectile import Projectile

# create the first class for the player
class Player(pygame.sprite.Sprite):    # sprite pour charger le joueur

    def __init__(self) :
        super().__init__()   # appel de la super class
        self.health = 100
        self.max_health = 100
        self.attack = 10     # point d'attaque / degats faits par le joueur
        self.velocity = 5    # vitesse du joueur
        self.all_projectiles = pygame.sprite.Group()     # groupe de projectiles
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()  # récupère un rectangle
        self.rect.x = 400     # en partant de gauche
        self.rect.y = 500     # en partant du haut


    def launch_projectile(self):     
        """launch the projectile
        """
        # projectile = Projectile()        # nouvelle instance
        # self.all_projectiles.add(projectile)   # ranger le projectile dans le groupe de projectile
        # remplace les 2 lignes de code ci-dessus
        self.all_projectiles.add(Projectile(self))

    def move_right(self):    # pour mouvement vers la droite
        self.rect.x += self.velocity   # récupérer la coordonnée x du joueur et ajouter la vitesse de déplacement du joueur

    def move_left(self):     # pour mouvement vers la gauche
        self.rect.x -= self.velocity   # récupérer la coordonnée x du joueur et retrancher la vitesse de déplacement du joueur

    



    
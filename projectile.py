import pygame

# define the class that create the projectile of the player
class Projectile(pygame.sprite.Sprite):

    # define the constructor
    def __init__(self, player):
        super().__init__()
        self.velocity = 5        # vitesse du projectile
        self.player = player     # pour récupérer valeurs du joueurs (ex: ses projectiles)
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50,50))     # scale = pour redimentionner une image en fonction des dimansions fournies entre ()
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120     # pour que le projectile soit à droite du joueur
        self.rect.y = player.rect.y + 80      # pour que le projectile soit au niveau de la main du joueur
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        """
            rotate projectile
        """
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)    # (surface, angle de rotation, scale =1)
        self.rect = self.image.get_rect(center=self.rect.center)     # pour que la rotation se fasse à partir du centre de l'image (enlever les sacades lors de l'affichage)


    def remove(self):
        """
            delete the projectile
        """
        self.player.all_projectiles.remove(self)      # supprimer le sprite qui vient de sortir de l'écran


    def move(self):
        """
            move the projectile
        """

        self.rect.x += self.velocity
        self.rotate()

        # check if the projectile is no more present on the screen
        if self.rect.x > 1080 :
            # if yes, delete the projectile 
            self.remove()
            print("\nsupprimé\n")





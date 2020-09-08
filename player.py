import pygame
from projectile import Projectile

# create the first class for the player
class Player(pygame.sprite.Sprite):    # sprite pour charger le joueur

    def __init__(self, game) :   # passer l'instance de la classe game dans les paramètres pour le récupérer comme attribut dans notre classe player
        super().__init__()   # appel de la super class
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10     # point d'attaque / degats faits par le joueur
        self.velocity = 5    # vitesse du joueur
        self.all_projectiles = pygame.sprite.Group()     # groupe de projectiles
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()  # récupère un rectangle
        self.rect.x = 400     # en partant de gauche
        self.rect.y = 500     # en partant du haut

    def damage(self, amount):
        # check if the player could have damage
        if self.health - amount > amount:
            self.health -= amount
        # if the player has no more life point
        else:
            self.game.game_over()


    def update_health_bar(self, surface):   # surface = l'endroit où on va placer la jauge
        # define a color for the life bar (green)
        bar_color = (111, 210, 46)

        # define a color for the background of the bar (grey)
        back_bar_color = (60, 63, 60)

        # define the position (X, Y) of the life bar, also the Weight (depend on life point) and the Height 
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 7]    # [X, Y, W, H] H = hauteur de la jauge en pixel
        
        # definir the position of the background of the life bar
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 7]

        # draw our life bar
        pygame.draw.rect(surface, back_bar_color, back_bar_position)    # mettre la jauge qui fait la longueur max (le fond gris) avant la jauge de vie pour que cette dernière soit visible
        pygame.draw.rect(surface, bar_color, bar_position)   # créer un rectangle sur la surface qu'on a récupérer avec une certaine couleur et à une certaine position


    def launch_projectile(self):     
        """launch the projectile
        """
        # projectile = Projectile()        # nouvelle instance
        # self.all_projectiles.add(projectile)   # ranger le projectile dans le groupe de projectile
        # remplace les 2 lignes de code ci-dessus
        self.all_projectiles.add(Projectile(self))

    def move_right(self):    # pour mouvement vers la droite
        # if the player isn't in collision with a monster, he could move
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity   # récupérer la coordonnée x du joueur et ajouter la vitesse de déplacement du joueur


    def move_left(self):     # pour mouvement vers la gauche
        self.rect.x -= self.velocity   # récupérer la coordonnée x du joueur et retrancher la vitesse de déplacement du joueur

    



    
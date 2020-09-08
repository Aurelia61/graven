import pygame
from player import Player     # depuis le fichier player importe la classe Player
from monster import Monster



# create a second class for the game
class Game:

    def __init__(self):
        # define if the game is starting or not
        self.is_playing = False
        # generate our player for new party
        self.player = Player(self)
        self.all_players = pygame.sprite.Group() 
        self.all_players.add(self.player)   # créer un groupe de sprite pour le joueur pour gérer la collision des monster avec le groupe player
        # group of monsters
        self.all_monsters = pygame.sprite.Group()      # crée un groupe de monstres (= sprite vierge)
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()     # générer un premier exemplaire au démarrage du jeu
        self.spawn_monster()     # pour faire aparaitre une second exemplaire de monster (attention modifier la position et la vitesse par rapport au premier monster, sinon ils vont être superposés)


    def game_over(self):
        # put the game to the beginning (put the monster off, life point player to 100, put the game in waiting)
        self.all_monsters = pygame.sprite.Group()   # pour écraser le groupe de monstres précédent
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # show the player
        screen.blit(self.player.image, self.player.rect)    # player.rect = placement du rectangle du joueur

        # update the life bar of the player
        self.player.update_health_bar(screen)

        # pick up projectiles of the player
        for projectile in self.player.all_projectiles:
            projectile.move()

        # pick up monsters
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)    # indiquer entre () l'endroit où l'on veut faire aparaitre la jauge

        # apply all images of the projectiles group on screen
        self.player.all_projectiles.draw(screen)

        # apply all the images of monster's group
        self.all_monsters.draw(screen)

        # check if the player want to go to the left or to the right
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width() :   
                # vérifier si la touche fléche droite est active ET inférieur à la largueur de l'écran + la taille du rectangle de l'image
            self.player.move_right()           # si oui activer la méthode bouger à droite du joueur
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:   # vérifier si la touche fléche gauche est active ET si le joueur ne se déplace pas au delà de l'écran
            self.player.move_left()  

    def check_collision(self, sprite, group):   # comparer un sprite avec un groupe de srpites
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)  # false car on ne veut pas que le joueur meurt

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)     # ajouter un monster au groupe de monstres



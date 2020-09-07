import pygame
from player import Player     # depuis le fichier player importe la classe Player
from monster import Monster


# create a second class for the game
class Game:

    def __init__(self):
        # generate our player for new party
        self.player = Player(self)
        self.all_players = pygame.sprite.Group() 
        self.all_players.add(self.player)   # créer un groupe de sprite pour le joueur pour gérer la collision des monster avec le groupe player
        # group of monsters
        self.all_monsters = pygame.sprite.Group()      # crée un groupe de monstres (= sprite vierge)
        self.pressed = {}
        self.spawn_monster()     # générer un premier exemplaire au démarrage du jeu
        self.spawn_monster()     # pour faire aparaitre une second exemplaire de monster (attention modifier la position et la vitesse par rapport au premier monster, sinon ils vont être superposés)

    def check_collision(self, sprite, group):   # comparer un sprite avec un groupe de srpites
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)  # false car on ne veut pas que le joueur meurt

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)     # ajouter un monster au groupe de monstres



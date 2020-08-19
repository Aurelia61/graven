import pygame
pygame.init()





# generate the window of the game
pygame.display.set_caption("Comet fall Game")     # display = affichage   # set_caption = pour changer le titre de la fenetre (et une icone)
screen = pygame.display.set_mode((1080,720))      # dimension de la fenetre(largueur et hauteur) # screen = SURFACE

# import game background
background = pygame.image.load('assets/bg.jpg') # = ARRIERE PLAN

# download the game
game = Game()


running = True     # variable sui contient si la fenetre est en cours d'execution ou non

# loop while running is true, the windows is opened
while running:

    # show the game background on a specific place on screen
    screen.blit(background, (-1000,-200))    #(largeur, hauteur # (0, 0) = au centre)

    # show the player
    screen.blit(game.player.image, game.player.rect)    # player.rect = placement du rectangle du joueur

    # update the window
    pygame.display.flip()

    # if the player close this windows
    for event in pygame.event.get(): # event.get() = pour savoir ce que le joueur est en train de faire ex: déplacement avec une touche
        # check if the event is " close the window"
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  # pour quitter l'application du jeu
            print("\nLa fenetre est fermée !\n")



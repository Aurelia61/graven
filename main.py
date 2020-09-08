import pygame
import math
from game import Game   # à partir du fichier game importe la class Game
pygame.init()


# generate the window of the game
pygame.display.set_caption("Comet fall Game")     # display = affichage   # set_caption = pour changer le titre de la fenetre (et une icone)
screen = pygame.display.set_mode((1080,720))      # dimension de la fenetre(largueur et hauteur) # screen = SURFACE

# import game background
background = pygame.image.load('assets/bg.jpg') # = ARRIERE PLAN

# import the banner of the game
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))   # transforme la taille de l'image (hauteur et largueur)
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)    # récupérer la largeur de l'écran est divisé par 4 pour mettre la banière au centre de l'écran

# import a button to play
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)    # un tier de la largeur
play_button_rect.y = math.ceil(screen.get_height() / 2 )

# download the game
game = Game()


running = True     # variable sui contient si la fenetre est en cours d'execution ou non

# loop while running is true, the windows is opened
while running:

    # show the game background on a specific place on screen
    screen.blit(background, (-1000,-200))    #(largeur, hauteur # (0, 0) = au centre)

    # check if the game has started or not
    if game.is_playing:
        # start the game
        game.update(screen)
    # check if the game isn't started
    else:
        # add the welcome screen
        # with the button play behind the banner
        screen.blit(play_button, play_button_rect)
        # show the banner
        screen.blit(banner, banner_rect)   # coordonnées du rectangle de la bannière ou mettre le typle(0,0) qui est la position en x et y


    # update the window
    pygame.display.flip()

    # get what the player has done
    for event in pygame.event.get(): # event.get() = pour savoir ce que le joueur est en train de faire ex: déplacement avec une touche
        # check if the event is " close the window"
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  # pour quitter l'application du jeu
            print("\nLa fenêtre est fermée !\n")
        # detect if the player release a key from the keypad
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecte if the space key is used to launch the projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        # detect if the key is no more used
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            # # get which key has been used
            # # if right arrow
            # if event.key == pygame.K_RIGHT:
            #     game.player.move_right()    # récupérer le player et le faire bouger vers la droite
            # # if left arrow
            # if event.key == pygame.K_LEFT:
            #     game.player.move_left()    # récupérer le player et le faire bouger vers la gauche

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if the mouse is in collision with the button play
            if play_button_rect.collidepoint(event.pos):    # si cette collision est vraie, cela veut dire que le joueur a cliqué sur le bouton
                # launch the game
                game.start()









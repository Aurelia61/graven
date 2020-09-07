import pygame
from game import Game   # à partir du fichier game importe la class Game
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

    # pick up projectiles of the player
    for projectile in game.player.all_projectiles:
        projectile.move()

    # pick up monsters
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)    # indiquer entre () l'endroit où l'on veut faire aparaitre la jauge

    # apply all images of the projectiles group on screen
    game.player.all_projectiles.draw(screen)

    # apply all the images of monster's group
    game.all_monsters.draw(screen)

    # check if the player want to go to the left or to the right
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width() :   
            # vérifier si la touche fléche droite est active ET inférieur à la largueur de l'écran + la taille du rectangle de l'image
        game.player.move_right()           # si oui activer la méthode bouger à droite du joueur
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:   # vérifier si la touche fléche gauche est active ET si le joueur ne se déplace pas au delà de l'écran
        game.player.move_left()  

    # update the window
    pygame.display.flip()

    # get what the player has done
    for event in pygame.event.get(): # event.get() = pour savoir ce que le joueur est en train de faire ex: déplacement avec une touche
        # check if the event is " close the window"
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  # pour quitter l'application du jeu
            print("\nLa fenetre est fermée !\n")
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







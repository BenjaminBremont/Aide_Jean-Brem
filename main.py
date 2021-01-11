import pygame
import math
from game import Game
pygame.init()

# Générer le fenêtre de notre jeu
pygame.display.set_caption("Aide Jean Brem")
screen = pygame.display.set_mode((1080, 720))

# Importer l'arriere plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# Importer charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Charger notre jeu
game = Game()

# Charger notre joueur
player = Player()

# import charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

running = True

# Boucle tant que cette condition est vraie
while running:

    # Appliquer la fenetre du jeu
    screen.blit(background, (0, -200))

    # vérifier si notre jeu a commencé ou non
    if game.is_playing:
        # déclencher les instructions de la partie
        game.update(screen)
    # vérifier si notre jeu n'a pas commencé
    else:
        # ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, (banner_rect))

# Mettre à jour l'écran
        pygame.display.flip()

        # Si le joueur ferme cette fenêtre
        for event in pygame.event.get():
            # que l'évènement est fermeture de fenêtre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("fermeture du jeu")

            # Détecter si un joueur lache une touche du clavier
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                # Détecter si la touche espace est enclenchée pour lancer notre projectile
                if event.type == pygame.K_SPACE:
                    game.player.launch_projectile()

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # vérification pour savoir si la souris est en collision avec le bouton joueur
                if play_button_rect.collidepoint(event.pos):
                    # Mettre le jeu en mode lancé
                    game.start()

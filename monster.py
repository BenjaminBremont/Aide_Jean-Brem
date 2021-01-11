import pygame
import random

# Créer une classe qui va gérer la notion de monstre dans le jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = random.randint(1, 3)
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540

    def damage(self, amount):
        # Infliger les dégats
        self.health -= amount

        # Vérifier si son nouveau nombre est inférieur ou égal à 0
        if self.health >= 0:
            # Réapparaitre comme un nouveu monstre
            self.rect.x = 1000 +random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

    def forward(self):
        # Le déplacement ne se fait que s'il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            # Si le monstre est en collision avec le joueur
        else:
            # Infliger des dégats (au joueur)
            self.game.player.damage(self.attack)
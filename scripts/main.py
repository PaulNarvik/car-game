"""Fichier principal du jeu. On importera dans celui-ci tous les modules créés """

# Modules déjà existants
import pygame
import time

# Initialisation du module Pygame qui gère la partie graphique du projet
pygame.init()

# Modules créés par nous
from game import Game
from text import Text
from button import Button

# Création d'une instance des classes
game = Game()

# Définition des couleurs de base
WHITE = "#ffffff"
BLACK = "#000000"
GRAY_0 = "#545454"
RED = "#ff0000"
GREEN = "#00ff00"
BLUE = "#0000ff"

# Boucle principale du jeu
while game.running:
    # Récupération de tous les évènements du jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.end()

    # Actualisation de l'état des  périphériques
    game.actualise_periph()

    # Effacement de tous ce qui est tracé
    game.screen.fill(GRAY_0)


    # Actualisation de l'affichage
    pygame.display.flip()
    game.clock.tick(game.FPS)

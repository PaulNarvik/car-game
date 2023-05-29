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

    #button = Button("color", "icon", 100, 100, 100, 100, bg_color=WHITE, icon_path="./assets/imgs/piece.png")
    button = Button(bg_type="image", content_type="text", pos_x=100, pos_y=100, len_x=200, len_y=200, bg_path="./assets/imgs/floor.png", text="Hello world", font="./assets/fonts/Chrusty.ttf", size=25, txt_color=WHITE)
    game.screen.blit(button.get_bg_surface(), button.get_bg_rect())
    game.screen.blit(button.get_content_surface(), button.get_content_rect())

    if button.get_bg_rect().collidepoint(game.mouse_pos) and game.mouse[0]:
        print("touched")
        time.sleep(0.1)
    
    #text = Text("Hello", "./assets/fonts/Chrusty.ttf", 25, BLACK, 100, 100)
    #game.screen.blit(text.get_surface(), text.get_rect())

    # Actualisation de l'affichage
    pygame.display.flip()
    game.clock.tick(game.FPS)

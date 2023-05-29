"""Fichier contenant la classe Game."""

import pygame
import sys

class Game:
    """Classe contenant les variables et méthodes relatives à la fenêtre et au jeu en général"""

    def __init__(self) -> None:
        # Caractéristiques du moniteur
        self.SCREEN_MAX_WIDTH = pygame.display.get_desktop_sizes()[0][1]
        self.SCREEN_WIDTH = round(self.SCREEN_MAX_WIDTH)
        self.SCREEN_HEIGHT = round(self.SCREEN_WIDTH * 9 / 16)
        
        # Création et réglage de la fenêtre
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Car Game")
        #pygame.display.set_icon()

        self.clock = pygame.time.Clock()
        self.FPS = 30

        # Initialise l'état des périphériques
        self.keys = None
        self.mouse = None
        self.mouse_pos = None

        # Variable principale permettant d'arrêter le jeu
        self.running = True

    def actualise_periph(self) -> None:
        """Actualise l'état de chaque périphériques (pressions et position)"""
        self.keys = pygame.key.get_pressed()

        self.mouse = pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()

    def end(self) -> None:
        """Fonction arrêtant tous les processus, appelée lorsque l'on tente de fermer la fenêtre"""
        self.running = False
        pygame.quit()
        sys.exit()
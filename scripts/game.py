"""Fichier contenant la classe Game."""

import pygame
import sys

class Game:
    """Classe contenant les variables et méthodes relatives à la fenêtre et au jeu en général"""

    def __init__(self) -> None:
        # Caractéristiques du moniteur et choix des dimensions
        self.SCREEN_MAX_SIZE = pygame.display.get_desktop_sizes()[0]
        self.SCREEN_WIDTH = round(self.SCREEN_MAX_SIZE[0] * 0.80)
        self.SCREEN_HEIGHT = round(self.SCREEN_WIDTH * 9 / 16)

        # Gestion du cas où la fenêtre dépasse de l'écran
        if self.SCREEN_HEIGHT > round(self.SCREEN_MAX_SIZE[1] * 0.95):
            self.SCREEN_HEIGHT = round(self.SCREEN_MAX_SIZE[1] * 0.9)
            self.SCREEN_WIDTH = round(self.SCREEN_HEIGHT * 16 / 9)

        # Création et réglage de la fenêtre
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Car Game")
        #pygame.display.set_icon()

        self.scenes = {}

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

    def get_marges(self) -> tuple[int, int]:
        """Fonction renvoyant la marge en fonction de la taille de l'écran (permet d'obtenir un ratio 16/9)"""
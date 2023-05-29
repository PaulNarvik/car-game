"""Fichier contenant la classe Text"""

# Modules déjà existants
import pygame

class Text:
    """
    Classe permettant de créer et afficher des éléments texte sur la fenêtre
    
    Paramètres d'entrées :
        - Paramètres obligatoires : 
            - text (str) : Texte qu'il faut créer sous forme de Surface
            - font (str) : Chemin vers la police à utiliser
            - size (int) : Taille du texte
            - color (tuple[int, int, int] | str) : Couleur du texte
        - Paramètres facultatifs : 
            - x (int) : Position X de l'origine du texte
            - y (int) : Position Y de l'origine du texte
    """
    
    def __init__(self, text : str, font : str, size : int, color : tuple[int, int, int] | str, x : int = 0, y : int = 0) -> None:
        self.text = text

        # Récupération de la police et assignation de la taille
        used_font = pygame.font.Font(font, size)

        # Création et édititon des coordonées
        self.surface = used_font.render(text, True, color)
        self.rect = self.surface.get_rect()
        self.rect.move_ip(x, y)

    def get_surface(self) -> pygame.Surface:
        """Renvoie l'objet Surface du texte"""
        return self.surface
    
    def get_rect(self) -> pygame.Rect:
        """Renvoie le Rect du texte"""
        return self.rect

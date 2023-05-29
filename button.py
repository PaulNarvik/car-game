"""Fichier contenant la classe Button"""

# Modules déjà existants
import pygame

# Modules créés par nous
from text import Text

class Button:
    """
    Classe qui associera un texte ou une image avec un rectangle de détection et une action

    Paramètres d'entrées :
        - Paramètres généraux : 
            - bg_type (str) : Type de fond de bouton ("color", "image")
            - content_type (str) : Type de contenu dans le bouton ("icon", "text")
            - pos_x (int) : Position X de l'origine du bouton (point en haut à gauche)
            - pos_y (int) : Position Y de l'origine du bouton (point en haut à gauche)
            - len_x (int) : Longueur du bouton sur l'axe X
            - len_y (int) : Longueur du bouton sur l'axe Y
            - target (str) : Action à réaliser à l'appui
        - Paramètre pour une image en fond : 
            - bg_path (str) : Chemin de l'image servant de fond
        - Paramètre pour une couleur en fond :
            - bg_color (tuple[int, int, int] | str) : Couleur du fond
        - Paramètres pour une icône en contenu :
            - icon_path (str) : Chemin de l'icône contenu dans le bouton
        - Paramètres pour un texte en contenu : 
            - text (str) : Texte contenu dans le bouton
            - font (str) : Police d'écriture du texte
            - size (int) : Taille du texte
            - txt_color (tuple[int, int, int] | str) : Couleur du texte
    """

    def __init__(self, bg_type : str, content_type : str, pos_x : int, pos_y : int, len_x : int, len_y : int, target : str, **kwargs : str | int | tuple[int, int, int]) -> None:
        # Analyse du type de fond
        if bg_type == "image":
            try:
                # Récupération du chemin de l'image
                bg_path = kwargs["bg_path"]
                # Récupération de l'image
                self.bg_surface = pygame.image.load(bg_path)
                self.bg_surface = pygame.transform.scale(self.bg_surface, (len_x, len_y))

            except KeyError:
                raise Exception("The bg_path argument is not specified for the background image in kwargs")

        elif bg_type == "color":
            try:
                # Récupération de la couleur de fond
                bg_color = kwargs["bg_color"]
                # Création de la surface qui servira de fond
                self.bg_surface = pygame.Surface((len_x, len_y))
                # Changement de la couleur de la surface
                self.bg_surface.fill(bg_color)

            except:
                raise Exception("The bg_color argument is not specified for the background color in kwargs")
        else:
            raise Exception("This type of background doesn't exist for button")
        
        # Place le fond sur l'écran
        self.bg_rect = self.bg_surface.get_rect()
        self.bg_rect.move_ip(pos_x, pos_y)

        # Analyse du type de contenu
        if content_type == "icon":
            try:
                # Récupération du chemin de l'icone
                icon_path = kwargs["icon_path"]
                # Récupération de l'image
                self.content_surface = pygame.image.load(icon_path)
                pygame.transform.scale(self.content_surface, (len_x, len_y))

            except KeyError:
                raise Exception("The icon_path argument is not specified for the icon in kwargs")
            
        elif content_type == "text":
            try: 
                # Récupération de tous les arguments
                self.text = kwargs["text"]
                font = kwargs["font"]
                size = kwargs["size"]
                txt_color = kwargs["txt_color"]
                # Création de l'élément texte
                self.content = Text(self.text, font, size, txt_color)
                self.content_surface = self.content.get_surface()

            except KeyError:
                raise Exception("At least one of the following arguments : \n- text\n- font\n- size\n- txt_color\n is not specified for the text in kwargs")
        else:
            raise Exception("This type of content_surface doesn't exist for button")
        
        # Centre le contenu 
        self.content_rect = self.content.get_rect()
        self.content_rect.move_ip(pos_x + (len_x - self.content_rect[2]) / 2, pos_y + (len_y - self.content_rect[3]) / 2)
    
    def get_bg_surface(self) -> pygame.Surface:
        """Renvoie l'object Surface qui correspond au fond du bouton"""
        return self.bg_surface
    
    def get_bg_rect(self) -> pygame.Rect:
        """Renvoie le Rect du bouton"""
        return self.bg_rect
    
    def get_content_surface(self) -> pygame.Surface:
        """Renvoie l'objet Surface du contenu du bouton"""
        return self.content_surface

    def get_content_rect(self) -> pygame.Rect:
        """Renvoie le Rect du contenu"""
        return self.content_rect
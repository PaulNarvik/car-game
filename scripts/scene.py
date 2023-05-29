"""Fichier contenant la classe Scène. Les instances sont crées au lancmeent de la fenêtre depuis game.py"""

class Scene:
    """
    Classe qui prend en argument tout le contenu qui sera affiché lorsque la scène sera active

    Paramètres d'entrées : 
        - Paramètre obligatoire : 
            - name (str) : Le nom qui identifiera la scène
        - Paramètres facultatifs : 
            - texts (list) : Liste de tous les textes à afficher
            - images (list) : Liste de toutes les images  à afficher
            - buttons (list) : Liste de tous les boutons à afficher
    """

    def __init__(self, name : str, **kwargs : list) -> None:
        self.name = name

        # Ajout de tout le contenu dans les différentes listes
        try:
            self.texts = kwargs["texts"]
        except KeyError:
            self.texts = []
        try:
            self.images = kwargs["images"]
        except KeyError:
            self.images = []
        try:
            self.buttons = kwargs["buttons"]
        except KeyError:
            self.buttons = []
        
"""Fichier contenant la classe Scène. Les instances sont crées au lancmeent de la fenêtre depuis game.py"""

class Scene:
    """
    Classe qui prend en argument tout le contenu qui sera affiché lorsque la scène sera active

    Paramètres d'entrées : 
        - Paramètre obligatoire : 
            - 
    """

    def __init__(self, name : str, **kwargs : list) -> None:
        if "texts" in kwargs:
            ...
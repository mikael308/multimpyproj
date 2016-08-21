import pygame
import src.resource.resource as resource
from src.view.game.gameobjects.gameobject import GameObject


class Trash(GameObject):
    """
    defines gameobject trashbin\n
    :author: Mikael Holmbom
    :version: 1.0
    """

    def __init__(self):
        dimen = resource.get_dimen("trash")
        src = resource.get_imagesrc("trash")
        img = pygame.image.load(src)
        img = pygame.transform.scale(img, dimen.wh())
        GameObject.__init__(self, img, dimen)


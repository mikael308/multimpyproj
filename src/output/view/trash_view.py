import pygame

import src.resource.resource as resource
from src.output.view.view_object import ViewObject


class TrashView(ViewObject):
    """
    Represents a gameobject trashbin\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def __init__(self, trash):

        src = resource.get_imagesrc("trash")
        img = pygame.image.load(src)
        img = pygame.transform.scale(img, trash.get_dimen().wh())

        ViewObject.__init__(self, img, trash)


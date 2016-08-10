import src.resource.resource as resource
import pygame
from gameobject import GameObject


class CPU(GameObject):
    """
    defines a CPU holding a value\n
    author Mikael Holmbom
    ver 1.0
    """

    # TEXT SURFACE
    __text_color = 0, 0, 0 # black
    __text_size = 30

    # this value
    __val = 0

    def __init__(self, val):
        src = resource.get_imagesrc("cpu")
        img = pygame.image.load(src)
        text = pygame.font.SysFont("val_label", self.__text_size)
        text_val = str(val)

        img.blit(text.render(text_val, 0, self.__text_color), (10, 5))

        GameObject.__init__(self, img)

        self.__val = val

    def get_val(self):
        """
        get this value
        :return: this value
        """
        return self.__val

    def __str__(self):
        return "CPU(" + str(self.get_val()) + ")"
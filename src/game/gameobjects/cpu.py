import src.resource.resource as resource
import pygame
from game_object import GameObject


class CPU(GameObject):
    """
    defines a CPU holding a value\n

    :author: Mikael Holmbom
    :version 1.0
    """

    # this value
    __adress = 0


    def __init__(self, adress):
        self.__adress = adress
        dimen = resource.get_dimen("cpu")
        rect = pygame.Rect(dimen.left, 0, dimen.diameter(), dimen.diameter())

        GameObject.__init__(self, dimen, rect)

    def get_adress(self):
        """
        get this value
        :return: this value
        """
        return self.__adress

    def __str__(self):
        return "CPU(" + str(self.get_adress()) + ")"

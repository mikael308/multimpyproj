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
    __adress = 0


    def __init__(self, adress):
        dimen = resource.get_dimen("cpu")
        self.__adress = adress
        src = resource.get_imagesrc("cpu")
        img = pygame.image.load(src)
        text = pygame.font.SysFont("val_label", self.__text_size)
        text_val = str(val)

        img.blit(text.render(text_val, 0, self.__text_color), (10, 5))
        GameObject.__init__(self, img, dimen)

    def __blit_adress(self, surf, dimen):
	"""
	blit the current address to param surf\n
	:param surf: the surface to blit
	:param dimen: the dimension blit
	"""
        text_val = str(self.get_adress())
        text_font = pygame.font.SysFont(self.__font_res.name, self.__font_res.size)

        text_surf = text_font.render(text_val, 0, self.__text_color)
        text_size = text_font.size(text_val)
        x = (dimen.radius) - (text_size[0] / 2)
        y = (dimen.radius) - (text_size[1] / 2)

        surf.blit(text_surf, (x, y))

    def get_adress(self):
        """
        get this value
        :return: this value
        """
        return self.__adress

    def __str__(self):
        return "CPU(" + str(self.get_adress()) + ")"

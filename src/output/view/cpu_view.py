import src.resource.resource as resource
import pygame
from view_object import ViewObject
from math import pi


class CPUView(ViewObject):
    """
    Represents a CPU holding a value\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    # TEXT SURFACE
    __text_color = 0, 0, 0 # black

    __font_res      = None


    def __init__(self, cpu):
        dimen = resource.get_dimen("cpu")
        r = dimen.radius

        # create surface
        col_fill = resource.get_color("cpu_fill").rgb()
        col_bord = resource.get_color("cpu_border").rgb()
        self.__font_res = resource.get_font("cpu")

        img = pygame.Surface((dimen.diameter(), dimen.diameter()), pygame.SRCALPHA, 32)
        img.convert_alpha(img)
        pygame.draw.circle(img, col_fill, (r, r), r)
        pygame.draw.arc(img, col_bord, img.get_rect(), 3*2/pi, 2*2 / pi, 5)

        ViewObject.__init__(self, img, cpu)

        # add the address on the surface
        self.__blit_adress(img, dimen)

    def __blit_adress(self, surf, dimen):
        """
        blit the current address to param surf\n
        :param surf: the surface to blit
        :param dimen: the dimension blit
        """
        text_val = str(self.get_gameobject().get_adress())
        text_font = pygame.font.SysFont(self.__font_res.name, self.__font_res.size)

        text_surf = text_font.render(text_val, 0, self.__text_color)
        text_size = text_font.size(text_val)
        x = (dimen.radius) - (text_size[0] / 2)
        y = (dimen.radius) - (text_size[1] / 2)

        surf.blit(text_surf, (x, y))


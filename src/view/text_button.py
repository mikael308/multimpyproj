import pygame
import src.resource.resource as resource
from button import Button


class TextButton(Button):
    """
    Clickable button containing a text label view\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    __font               = None
    __text_content      = ""

    __text_color        = None

    def __init__(self, text_content, dimen=resource.get_dimen("text_button")):
        """

        :param text_content:
        """

        src = resource.get_imagesrc("button")

        main_surf = pygame.Surface((dimen.width, dimen.height), pygame.SRCALPHA, 32)

        btn_surf = pygame.image.load(src)
        btn_surf = pygame.transform.scale(btn_surf, (dimen.width, dimen.height))

        main_surf.blit(btn_surf, (0,0))

        pygame.font.init()
        self.__text_content = text_content.upper()
        font_res = resource.get_font("menu_button")
        self.__font = pygame.font.SysFont(font_res.name, font_res.size)

        self.__text_color = (0, 0, 0)

        text_surface = self.__font.render(self.__text_content, 0, self.__text_color)
        text_x = (dimen.width / 2) - (self.__font.size(self.__text_content)[0] / 2)
        text_y = (dimen.height / 2) - (self.__font.size(self.__text_content)[1] / 2)

        main_surf.blit(text_surface, (text_x, text_y))
        main_surf.convert_alpha(main_surf)

        Button.__init__(self, main_surf, dimen)

    def get_text(self):
        """
        get the text content of this button
        :return:
        """
        return self.__text_content




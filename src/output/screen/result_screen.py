import pygame

import src.resource.resource as resource
from src.output.screen.view_screen import ViewScreen


class ResultScreen(ViewScreen):
    """
    Screen used for use-case: result\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    __game_controller    = None

    __article_player= None

    __background_color = resource.get_color("resultscreen_background").rgb()

    __text_color    = resource.get_color("resultscreen_text").rgb()

    __header_result = resource.get_string("result_header_player")


    def __init__(self):
        ViewScreen.__init__(self)
        self._article_padd = resource.get_dimen("result_article_padd")

    def set_game_controller(self, game_controller):
        self.__game_controller = game_controller

    def setup(self):
        ViewScreen.setup(self)

        self._get_background().fill(self.__background_color)

        self._font_res      = resource.get_font("result_playerinfo")
        self._font          = pygame.font.SysFont(self._font_res.name, self._font_res.size, self._font_res.style_bold, self._font_res.style_italic)
        self._font_res_header = resource.get_font("result_header")
        self._font_header   = pygame.font.SysFont(self._font_res_header.name, self._font_res_header.size, self._font_res_header.style_bold,self._font_res_header.style_italic)

        self.__article_player = self.__create_playerinfo_view()

    def __create_playerinfo_view(self):
        """
        create article displaying player result
        :return:
        """
        player = self.__game_controller.get_player()

        rows = []
        rows.append("score : " + str(player.get_score()))
        rows.append("level : " + str(player.get_level()))

        header = self.__header_result.upper()
        width, height = self._get_article_size(header, rows)
        surf = pygame.Surface((width, height))
        surf.fill((255, 255, 255))

        self._blit_rows(surf, header, self.__text_color, rows)

        return surf

    def render(self):
        ViewScreen.render(self)

        mainsurf = self._get_main_surface()
        mainsurf.blit(self.__article_player, (10,10))

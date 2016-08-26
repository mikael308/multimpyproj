import pygame

import src.resource.resource as resource
import src.settings.game_controls as game_controls
import src.settings.navigation_controls as nav_controls
import src.tools as tools
from src.output.screen.view_screen import ViewScreen


class InfoScreen(ViewScreen):
    """
    screen used for use-case info\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    __text_color        = resource.get_color("info_text").rgb()

    __article_background_color = resource.get_color("info_article_background").rgb()

    __controls_view     = None
    __controls_dimen    = resource.get_dimen("info_article_controls")
    __gameinfo_view     = None
    __gameinfo_dimen    = resource.get_dimen("info_article_gameinfo")

    __gameinfo_header_value = resource.get_string("info_header_gameinfo")
    __controls_header_value = resource.get_string("info_header_controls")

    def __init__(self):
        """

        """
        dimen_window = resource.get_dimen("main_window")
        ViewScreen.__init__(self, dimen_window)

        self._font_res     = resource.get_font("info")
        self._font         = pygame.font.SysFont(self._font_res.name, self._font_res.size)
        self._font_header  = pygame.font.SysFont(self._font_res.name, self._font_res.size, True)
        self._article_padd  = resource.get_dimen("info_article_padd")

    def setup(self):
        """

        :return:
        """
        ViewScreen.setup(self)
        self._get_background().fill(resource.get_color("infoscreen_background").rgb())

        self.update()

    def update(self):
        """

        :return:
        """
        self.__controls_view = self.__create_controls_view()
        self.__gameinfo_view = self.__create_gameinfo_view()

    def render(self):
        """

        :return:
        """
        main_surf = self._get_main_surface()
        main_surf.blit(self._get_background(), (0, 0))

        main_surf.blit(self.__controls_view, self.__controls_dimen.pos())
        main_surf.blit(self.__gameinfo_view, self.__gameinfo_dimen.pos())

    def __create_controls_view(self):
        """
        creates a Surface containing controls information\n
        :return:
        """
        rows = []
        rows.append("__GAME__")
        rows.append("left: '" + pygame.key.name(game_controls.key_mov_left) + "'")
        rows.append("up: '" + pygame.key.name(game_controls.key_mov_up) + "'")
        rows.append("right: '" + pygame.key.name(game_controls.key_mov_right) + "'")
        rows.append("down: '" + pygame.key.name(game_controls.key_mov_down) + "'")
        rows.append("grab/release packets: '" + pygame.key.name(game_controls.key_pickup) + "'")
        rows.append("enabled/disable sound effects: '" + pygame.key.name(game_controls.key_switch_sound_enabled) + "'")
        rows.append("")

        rows.append("__NAVIGATION__")
        rows.append("back: '" + pygame.key.name(nav_controls.key_back) + "'")
        rows.append("exit: '" + pygame.key.name(nav_controls.key_quit) + "'")

        header = self.__controls_header_value.upper()
        width, height = self._get_article_size(header, rows)
        surf = pygame.Surface((width, height))
        surf.fill(self.__article_background_color)

        self._blit_rows(surf, header, self.__text_color, rows)

        return surf

    def __create_gameinfo_view(self):
        """
        creates a Surface containing gameinfo\n
        :return:
        """

        text_content = resource.get_string("info_gameinfo_text")
        rows = tools.divide_to_rows(resource.get_value("info_gameinfo_maxwidth"), text_content)

        header = self.__gameinfo_header_value.upper()
        article_dimen_wh = self._get_article_size(header, rows)

        surf = pygame.Surface(article_dimen_wh)
        surf.fill(self.__article_background_color)

        self._blit_rows(surf, header, self.__text_color,rows)

        return surf


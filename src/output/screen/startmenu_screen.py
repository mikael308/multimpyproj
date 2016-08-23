import pygame

import src.resource.resource as resource
from src.output.screen.screen import Screen
from src.output.view.text_button import TextButton


class StartMenuScreen(Screen):
    """
    Screen used for use-case: result\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    __btns              = None

    __text              = None
    __text_dimen          = None


    def __init__(self):
        dimen_window = resource.get_dimen("main_window")
        Screen.__init__(self)

        self.__btns = {}

    def setup(self):
        """
        initiates this screens attributes\n
        :return: None
        """
        Screen.setup(self)
        self._get_background().fill(resource.get_color("startmenu_background").rgb())

        self.__btns["START"]    = TextButton(resource.get_string("btn_start_text"))
        self.__btns["INFO"]     = TextButton(resource.get_string("btn_info_text"))
        self.__btns["EXIT"]     = TextButton(resource.get_string("btn_exit_text"))

        screen_mid_w = (self.get_width() / 2)

        # game title
        dimen_title     = resource.get_dimen("startscreen_title")
        game_title      = resource.get_string("game_title")
        font_res        = resource.get_font("startscreen_title")
        col = resource.get_color("startmenu_gametitle").rgb()
        font = pygame.font.SysFont(font_res.name, font_res.size)

        self.__text = font.render(game_title, 0, col)
        self.__text_dimen = resource.get_dimen("startscreen_title")
        self.__text_dimen.x = screen_mid_w - dimen_title.width

        # set buttons position
        button_marg = resource.get_dimen("button_marg")
        for i, btn in enumerate(self.get_btns().itervalues()):
            x = screen_mid_w - (btn.get_width() / 2)
            y = button_marg.top + ((i + 1) * button_marg.dist)
            btn.set_pos(x, y)

    def update(self):
        """

        :return:
        """
        pass

    def render(self):
        """
        render this screen\n
        :return: None
        """
        Screen.render(self)

        self._blit(self.__text, (self.__text_dimen.pos()))

        for i, btn in enumerate(self.get_btns().itervalues()):
            self._blit(btn)

    def get_btns(self):
        """
        get the buttons in this screen
        :return:
        """
        return self.__btns


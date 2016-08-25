import pygame

import src.resource.resource as resource
from gamefield_screen import GameFieldScreen
from src.output.screen.screen import Screen
from src.output.view.infopanel import InfoPanel
from src.output.view.switch_button import SwitchButton


class GameScreen(Screen):
    """
    defines screen for use-case game\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    __btns                  = None

    __infopanel             = None
    __infopanel_dimen       = resource.get_dimen("infopanel")

    __gamefield_screen      = None

    __game_controller       = None

    __background_color      = resource.get_color("gamescreen_background").rgb()

    __scaling_factor_x      = 0
    __scaling_factor_y      = 0

    def __init__(self, dimen=resource.get_dimen("gamescreen")):

        Screen.__init__(self, dimen)

        self.__infopanel = InfoPanel()

        self.__gamefield_screen = GameFieldScreen()

        self.__btns = {}

        # setup background
        self._set_background(pygame.Surface(self.get_dimen().wh()))
        self._get_background().fill(self.__background_color)

        # init the dimension of the gamefield
        dimen_gamefield = resource.get_dimen("gamefieldscreen")
        self.__gamescreen_margin_left = (self.get_dimen().width / 2) - (dimen_gamefield.width / 2)
        self.__gamescreen_margin_top = (self.get_dimen().height / 2) - (dimen_gamefield.height / 2)

        self.__btns["SOUND"] = self.__create_soundfx_button()

    def get_scaling_factors(self):
        """
        get the scaling factors acording to this size\n
        :return: scaling factors as tuple (x, y)
        """
        return self.__scaling_factor_x, self.__scaling_factor_y

    def __create_soundfx_button(self):
        """
        create a soundfx switchbutton instance\n
        :return: SwitchButton instance
        """
        switch_btn_dimen = resource.get_dimen("sound_switch_button")
        btn_surf_on = pygame.image.load(resource.get_imagesrc("soundfx_on"))
        btn_surf_off = pygame.image.load(resource.get_imagesrc("soundfx_off"))

        return SwitchButton(btn_surf_on, btn_surf_off, switch_btn_dimen)

    def scale_pos(self, (x, y)):
        """
        scale a logic position to screen position
        :return: modified position as tuple (x, y)
        """
        return (x * self.get_scaling_factors()[0]), (y * self.get_scaling_factors()[1])

    def get_infopanel(self):
        """
        get this infopanel
        :return: infopanel attr instance
        """
        return self.__infopanel

    def set_game_controller(self, game_controller):
        """
        set a game_controller to get all viewing objects from
        :param game_controller:
        :return: None
        """
        self.__game_controller = game_controller
        self.__gamefield_screen.set_game_controller(game_controller)

    def click(self, pos):
        """
        delegate a click on this screen at position param pos\n
        :param pos: the position of the click
        :return: None
        """
        for b in self.get_btns().itervalues():
            print "r: " + str(b.get_rect().x) + ", " + str(b.get_rect().y)
            if b.get_rect().collidepoint(pos):
                b.click()
                break

    def setup(self):
        """
        setup screens attributes
        :return: None
        """
        Screen.setup(self)

        sound_btn = self.get_btns()["SOUND"]

        self.__gamefield_screen.setup()

        if self.get_infopanel() is not None:
            self.get_infopanel().set_player(self.__game_controller.get_player())

        self.update()

    def update(self):
        self.__gamefield_screen.update()


    def render(self):
        """

        :return: None
        """

        self._blit(self._get_background(), (0, 0))

        self._get_main_surface().blit(self.__gamefield_screen.render(), (self.__gamescreen_margin_left, self.__gamescreen_margin_top))

        self._blit(self.__infopanel.render(), self.__infopanel_dimen.pos())
        for b in self.__btns.itervalues():
            self._blit(b)

    def get_btns(self):
        """
        get the existing buttons in this screen\n
        :return: dictionary of button instances
        """
        return self.__btns

    def get_gamefield(self):
        """
        get this gamefield screen\n
        :return: this GameFieldScreen instance
        """
        return self.__gamefield_screen

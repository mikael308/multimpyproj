import pygame
import src.resource.resource as resource
from src.game.gameobjects.game_object import GameObject
from src.output.view.view_object import ViewObject


class Screen:
    """

    :Example:\n
    typical usecase:\n
    * __init__()
    * set_  objects
    * setup()
    - 1: [update the games objects]
    - 2: if new objects in buffer -> update()
    - 3: render()
    - 4: if end_event: quit
    - else: goto 1.

    :author: Mikael Holmbom
    :ver: 1.0
    """
    __dimen             = None

    __main_surface      = None

    __background        = None

    def __init__(self, dimen=resource.get_dimen("main_window"), set_display_mode_dimen=True):
        pygame.init()
        self.__dimen = dimen
        if set_display_mode_dimen:
            self.__main_surface     = pygame.display.set_mode(dimen.wh())
        else:
            self.__main_surface = pygame.Surface(dimen.wh())

        self.__background = pygame.Surface(dimen.wh())

    def close(self):
        """
        close this screen\n
        closing the pygame resources\n
        :return: None
        """
        pygame.font.quit()
        pygame.display.quit()

    def _get_main_surface(self):
        """
        get the main_surface of this current screen\n
        :return: the main surface of this screen
        :returns: pygame.Surface
        """
        return self.__main_surface

    def setup(self):
        """
        initialize values for all the objects in this screen
        :return: None
        """
        pass

    def click(self, pos):
        """
        make a mouseclick on this screen at position\n
        :param pos:
        :return: None
        """
        pass

    def _blit(self, object, pos=None):
        """
        displays object on current screen
        :param object: object to display
        :type object: GameObject
        :return: None
        """

        surf = None
        if isinstance(object, ViewObject):
            if pos is None:
                pos = object.get_pos()
            surf = object.get_image()

        elif isinstance(object, Screen):
            if pos is None:
                pos = object.get_dimen().pos()
            surf = object.render()

        else:
            if pos is None:
                pos= (0, 0)
            surf = object

        self.__main_surface.blit(surf, pos)

    def update(self):
        """
        update the objects displayed on screens\n
        :return: None
        """
        raise NotImplemented("abstract method not implemented yet")

    def render(self):
        """
        display all current objects on current screen\n
        :return: None
        """
        self._get_main_surface().blit(self._get_background(), (0, 0))

    def get_dimen(self):
        return self.__dimen

    def get_width(self):
        """
        return the screens width\n
        :return: main surface width
        """
        return self.__main_surface.get_width()

    def get_height(self):
        """
        returns the screens height\n
        :return: main surface height
        """
        return self.__main_surface.get_height()

    def _get_background(self):
        """
        get this background surface\n
        :return: current background
        :returns: pygame.Surface
        """
        return self.__background

    def _set_background(self, background):
        """
        set this current background surface\n
        :param background: new background
        :type background: pygame.Surface
        :return: None
        """
        self.__background = background

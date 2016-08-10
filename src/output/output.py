import resource
from screen import Screen
from sound_controller import SoundController


class Output:
    """
    facade object handling all output
    contain parts:
        * Screen - visual output
        * SoundController - audiovisual output

    :author: Mikael Holmbom
    :version: 1.0
    """

    __soundcontroller   = None
    __screen            = None

    def __init__(self):
        size = (resource.get_dimen("main_window_size_width"),
                resource.get_dimen("main_window_size_height"))

        self.__screen = Screen(size)
        self.__screen.setup()

    def close(self):
        """
        closes this resource
        :return:
        """
        self.__screen.close()
        self.get_soundcontroller().close()

    def get_soundcontroller(self):
        """
        get soundengine
        :return: this SoundController instance
        :returns: SoundController
        """
        return self.__soundcontroller

    def get_screen(self):
        """
        get the screen
        :return:
        """
        return self.__screen

    def render(self):
        """
        renders output
        :return:
        """
        self.__screen.render()

    def _set_soundcontroller(self, soundcontroller):
        """
        set this soundcontroller
        :param soundcontroller: new SoundController instance
        :type soundcontroller: SoundController
        :return: None
        """
        self.__soundcontroller = soundcontroller

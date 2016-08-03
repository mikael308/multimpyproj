import resource
from soundengine import SoundEngine
from screen import Screen


class Output:
    """
    facade object handling all output

    :author: Mikael Holmbom
    :version: 1.0
    """

    __soundengine       = None
    __screen            = None

    def __init__(self):
        size = (resource.get_dimen("main_window_size_width"),
                resource.get_dimen("main_window_size_height"))

        self.__screen = Screen(size)
        self.__screen.setup()

        self.__soundengine = SoundEngine()

    def close(self):
        """
        closes this resource
        :return:
        """
        self.__screen.close()
        self.__soundengine.close()

    def get_soundengine(self):
        """
        get soundengine
        :return:
        """
        return self.__soundengine

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

    def update(self):
        """
        updates output
        :return:
        """
        self.__screen.update()

    def level_up(self):
        """
        outputs level up
        :return:
        """
        self.__soundengine.play("level_up")

    def score(self):
        """
        outputs score
        :return:
        """
        self.__soundengine.play("score")

    def wrong_cpu(self):
        """
        outputs wrong cpu
        :return:
        """
        self.__soundengine.play("wrong_cpu")

    def buffer_overflow(self):
        """
        outputs buffer overflow
        :return:
        """
        self.__soundengine.play("buffer_overflow")
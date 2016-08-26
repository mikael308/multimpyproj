import pygame
from src.activable import Activable


class Controller(Activable):
    """
    Controller instance holding data about current use-case\n
    instance that can be manipulated\n

    state can be changed with public methods:
        * start() set instance to running
        * setup(self) set instance to running
        * stop(self) set instance to not running
        * shutdown(self) set instante to not running and close display

    :author: Mikael Holmbom
    :version: 1.0
    """


    def __init__(self):
        """

        """
        pass


    def setup(self):
        """
        setup this controller\n
        controller sets to state running\n
        :return: None
        """
        self.start()

    def shutdown(self):
        """
        shuts down this controller, calling this will stop the current window display\n
        state is set to not running\n
        :return: None
        """
        self.stop()
        if self.has_output():
            self.get_output().shutdown()

        pygame.quit()

        """
        :return:
        """

        """
        """

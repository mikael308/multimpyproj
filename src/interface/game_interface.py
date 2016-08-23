import pygame

from interface import Interface
from src.controller.game_controller import GameEngine
from src.event.game_eventhandler import GameEventHandler
from src.event.result_eventhandler import ResultEventHandler
from src.output.game_output import GameOutput
from src.output.result_output import ResultOutput


class GameInterface(Interface):
    """
    interface for use-case: Game\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def __init__(self):
        Interface.__init__(self)
        eh      = GameEventHandler(self)
        e       = GameEngine()
        out     = GameOutput(e)

        self._set_engine(e)
        self._set_eventhandler(eh)
        self._set_output(out)

    def setup(self):
        Interface.setup(self)
        e   = self.get_engine()
        out = self.get_output()

        out.get_screen().get_infopanel().set_player(e.get_player())

    def run(self):
        Interface.run(self)

        if pygame.display.get_init():
            self._set_eventhandler(ResultEventHandler(self))
            out = ResultOutput()
            out.get_screen().set_gameengine(self.get_engine())

            self._set_output(out)
            Interface.setup(self)

            Interface.run(self)

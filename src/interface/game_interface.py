
from interface import Interface
from src.controller.game_controller import GameController
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
        eh      = GameEventHandler()
        c       = GameController()
        out     = GameOutput(c)

        c.set_output(out)
        eh.set_controller(c)

        self._set_controller(c)
        self._set_eventhandler(eh)
        self._set_output(out)

    def setup(self):
        Interface.setup(self)
        e   = self.get_controller()
        out = self.get_output()

        out.get_screen().get_infopanel().set_player(e.get_player())

    def run(self):
        #run the gameplay
        Interface.run(self)

        endstate = self.get_controller().get_endstate()

        if endstate.is_active():
            # if game controller has a valid endstate, show the result
            self._show_result(endstate)

    def _show_result(self, endstate):
        """
        displays result_interface displaying the endstate result\n
        :param endstate: endstate result to display
        :return: None
        """
        eh = ResultEventHandler()
        eh.set_controller(self.get_controller())
        self._set_eventhandler(eh)
        out = ResultOutput()
        out.set_endstate(endstate)

        self._set_output(out)
        self.get_controller().start()
        self.get_output().setup()

        Interface.run(self)


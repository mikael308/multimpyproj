from interface import Interface
from src.engine.startmenu_engine import StartMenuEngine
from src.event.startmenu_eventhandler import StartMenuEventHandler
from src.interface.game_interface import GameInterface
from src.interface.info_interface import InfoInterface
from src.output.startmenu_output import StartMenuOutput


class StartMenuInterface(Interface):
    """
    interface for use-case: startmenu\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def __init__(self):
        """

        :param interface:
        """
        eh = StartMenuEventHandler(self)
        e = StartMenuEngine()
        out = StartMenuOutput()

        self._set_engine(e)
        self._set_eventhandler(eh)
        self._set_output(out)

    def setup(self):
        """

        :return:
        """
        Interface.setup(self)

        btns = self.get_output().get_btns()

        def click_start():
            i = GameInterface()
            i.setup()
            i.run()

        def click_info():
            i = InfoInterface()
            i.setup()
            i.run()

        def click_exit():
            self.get_engine().shutdown()

        btns["START"].set_on_click_listener(click_start)
        btns["INFO"].set_on_click_listener(click_info)
        btns["EXIT"].set_on_click_listener(click_exit)


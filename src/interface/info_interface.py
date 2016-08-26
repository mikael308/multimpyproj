from interface import Interface
from src.controller.info_controller import InfoController
from src.event.info_eventhandler import InfoEventHandler
from src.output.info_output import InfoOutput


class InfoInterface(Interface):
    """
    Interface for use-case: info\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def __init__(self):
        """

        """
        eh = InfoEventHandler()
        c = InfoController()
        out = InfoOutput()

        eh.set_controller(c)

        self._set_controller(c)
        self._set_eventhandler(eh)
        self._set_output(out)

from interface import Interface
from src.controller.info_controller import InfoEngine
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
        eh = InfoEventHandler(self)
        e = InfoEngine()
        out = InfoOutput()

        self._set_engine(e)
        self._set_eventhandler(eh)
        self._set_output(out)

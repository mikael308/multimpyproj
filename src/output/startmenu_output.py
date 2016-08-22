from src.output.output import Output
from src.output.screen.startmenu_screen import StartMenuScreen


class StartMenuOutput(Output):
    """
    output facade used for use-case startmenu\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def __init__(self):
        Output.__init__(self)

        self._set_screen(StartMenuScreen())

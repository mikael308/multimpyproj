from src.output.output import Output
from src.output.screen.info_screen import InfoScreen


class InfoOutput(Output):
    """
    output facade used for use-case info\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def __init__(self):
        Output.__init__(self)

        self._set_screen(InfoScreen())

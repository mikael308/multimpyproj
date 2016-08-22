from src.output.output import Output
from src.output.screen.result_screen import ResultScreen


class ResultOutput(Output):
    """
    output facade used for use-case: result\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def __init__(self):
        Output.__init__(self)

        self._set_screen(ResultScreen())


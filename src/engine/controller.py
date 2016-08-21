

class Engine:
    """
    Engine instance holding data about current use-case\n
    instance that can be manipulated

    engine can be in states:
        * running
        * not running
    determine state with public method:
        * is_running(self)
    state can be changed with public methods:
        * setup(self)
        * shutdown(self)

    :author: Mikael Holmbom
    :version: 1.0
    """

    # the current state of this engine
    __is_running        = None

    def __init__(self):
        """

        """
        pass

    def _set_to_running(self):
        """
        set this engine to state: running
        :return: None
        """
        self.__is_running = True

    def _stop_running(self):
        """
        set this engine to state: not running
        :return: None
        """
        self.__is_running = False

    def setup(self):
        """
        setup this engine\n
        engine sets to state running\n
        :return: None
        """
        self._set_to_running()

    def shutdown(self):
        """
        shuts down this engine\n
        state is set to not running\n
        :return: None
        """
        self._stop_running()

    def is_running(self):
        """
        determine if this controller is in state running\n
        :return: True if current state is: running
        """
        return self.__is_running == True
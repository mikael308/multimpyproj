

class Activable():
    """
    instance that can be in two states
    * active
    * disabled


    :author: Mikael Holmbom
    :version: 1.0
    """

    # the current state of this instance
    __is_active        = False


    def activate(self):
        """
        set this controller to state: running
        :return: None
        """
        self.__is_active = True

    def deactivate(self):
        """
        set this controller to state: not running
        :return: None
        """
        self.__is_active = False

    def stop(self):
        """
        stops this instance\n
        :return:
        """
        self.deactivate()

    def start(self):
        """
        start this instance\n
        :return:
        """
        self.activate()

    def is_active(self):
        """
        determine if this instance is in state active\n
        :return: True if current state is: active
        """
        return self.__is_active == True

    def is_disabled(self):
        """
        determine if this instance is in state disabled\n
        :return: True if current state is: disabled
        """
        return self.__is_active == False
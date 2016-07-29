from GameObject import GameObject


class Attachable(GameObject):
    """
    defines object ability to attach and detach other objects\n

    author Mikael Holmbom
    ver 1.0
    """

    # the attached object
    __attached_obj = None

    def __init__(self, sprite):
        """

        :param sprite:
        """
        GameObject.__init__(self, sprite)

    def attach(self, gameobj):
        """
        attach object to this object\n
        :param gameobj: the object to attach
        :return:
        """
        self.__attached_obj = gameobj

    def detach(self):
        """
        detach the current attach object\n
        :return: True if there was a prior attached object that now is removed
        """
        if self.__attached_obj is None:
            return False
        else:
            self.__attached_obj = None
            return not self.has_attached()

    def get_attached(self):
        """
        get the attached object\n
        :return: the attached object
        """
        return self.__attached_obj

    def has_attached(self):
        """
        determine if this has a attached object\n
        :return: True if this has a attached object
        """
        return self.__attached_obj is not None
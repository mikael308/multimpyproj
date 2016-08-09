

class Attachable:
    """
    defines object ability to attach and detach other objects\n

    author Mikael Holmbom
    ver 1.0
    """

    # the attached object
    __attached_obj = None

    def __init__(self):
        """

        """

    def move_pos(self, x, y):
        """
        move current position\n
        :param x: X-axis direction
        :param y: Y-axis direction
        :return:
        """
        if self.has_attached():
            self.get_attached().move_pos(x, y)

    def attach(self, gameobj):
        """
        attach object to this object\n
        :param gameobj: the object to attach
        :return: True if object was attached correct; False if this already had attached object in prior of call
        """
        if self.has_attached():
            return False
        self.__attached_obj = gameobj
        return self.has_attached()

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

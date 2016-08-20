

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
        :return: the attached object, None if this does not have a attached object
        """
        if self.__attached_obj is None:
            return None
        else:
            tmp_obj = self.get_attached()
            self.__attached_obj = None
            return tmp_obj

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

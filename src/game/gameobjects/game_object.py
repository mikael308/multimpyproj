import pygame


class GameObject:
    """
    represents a object used in gameplay\n
    
    :author: Mikael Holmbom
    :version: 1.0
    """

    __dimen = None

    __rect = None

    def __init__(self, dimen, rect=None):
        self.__dimen = dimen

        if rect is not None:
            self.__rect = rect
        else:
            # create the rect from arg dimen
            self.__rect = pygame.Rect(dimen.rect())

    def get_dimen(self):
        """
        get this dimension\n
        :return:
        """
        return self.__dimen

    def get_rect(self):
        """
        get this rect\n
        :return:
        """
        return self.__rect

    def move_pos(self, x, y):
        """
        move current position\n
        :param x: X-axis direction\n
        :type x: int
        :param y: Y-axis direction\n
        :type y: int
        :return: None
        """
        mod_rect = self.get_rect().move((x, y))
        self.set_rect(mod_rect)

        self.__dimen.x = mod_rect.x
        self.__dimen.y = mod_rect.y

    def set_pos(self, x, y):
        """
        set object to absolute position
        :param x: x-axis position
        :type x: int
        :param y: y-axis position
        :type y: int
        :return: None
        """

        self.get_rect().x = x
        self.get_rect().y = y

        self.__dimen.x = x
        self.__dimen.y = y

    def set_rect(self, rect):
        """
        set this rect\n
        :param rect: new rect\n
        :type rect: pygame.Rect
        :return: self
        """
        self.__rect = rect
        return self

    def get_pos(self):
        """
        get this position
        :return:
        """
        return self.get_rect().x, self.get_rect().y


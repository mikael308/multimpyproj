import pygame
from button import Button
import src.resource.resource as resource


class SwitchButton(Button):
    """
    Clickable button holding on/off value state\n
    to switch value: see switch(self)\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    __switch_val = None

    __image_off = None
    __image_on = None

    def __init__(self, surf_off, surf_on, dimen=resource.get_dimen("switch_button")):
        """

        :param surf_off: surface to display if this is switch value is False
         :type surf_off: pygame.Surface
        :param surf_on: surface to display if this is switch value is True
         :type surf_on: pygame.Surface
        :param dimen: the dimension of this button
        """
        if surf_off.get_width() is not dimen.width \
                or surf_off.get_height() is not dimen.height:
            surf_off = pygame.transform.scale(surf_off, dimen.wh())

        if surf_on.get_width() is not dimen.width \
                or surf_on.get_height() is not dimen.height:
            surf_on = pygame.transform.scale(surf_on, dimen.wh())

        Button.__init__(self, surf_off, dimen)

        self.__switch_val   = False

        self.__image_off    = surf_off
        self.__image_on     = surf_on

    def get_images(self):
        """
        get the images of this instance
        :return:
        """
        return self.__image_off, self.__image_on

    def is_switch_on(self):
        """
        determine if this button instance is switched on
        :return:
        """
        return self.__switch_val

    def switch(self):
        """
        switch this button instance\n
        :return:
        """
        self.__switch_val = not self.__switch_val
        if self.is_switch_on():
            self._set_image(self.__image_on)
        else:
            self._set_image(self.__image_off)

import pygame
import tools
import src.resource.resource as resource
from view_object import ViewObject
from packet_view import PacketView


class BufferView(ViewObject):
    """
	Represents the the buffer\n

	:author: Mikael Holmbom
	:version: 1.0
    """

    __background_color = resource.get_color("buffer_view_background").rgb()
    __background_surface = None

    __dimen         = resource.get_dimen("buffer_view")
    __dimen_border  = resource.get_dimen("buffer_view_border")
    __dimen_padd    = resource.get_dimen("buffer_view_padd")

    __image = None

    def __init__(self, buffer):

        self.__background_surface = self.create_background()

        ViewObject.__init__(self, self.__background_surface)
        self.set_gameobject(buffer)

        pos = self.__dimen.x, self.__dimen.y
        self.set_rect(pygame.Rect(pos, self.__dimen.wh()))

    def create_background(self):
        """
        creates a background for this buffer
        :return:
        """
        buf_cap = resource.get_value("buffer_capacity")
        packet_dimen = resource.get_dimen("packet")
        padd = self.__dimen_padd

        self.__dimen.width = (padd.left * 2) + packet_dimen.width
        self.__dimen.height = ((packet_dimen.height + self.__dimen.dist) * buf_cap) + (padd.top * 2)

        surf = pygame.Surface(self.__dimen.wh())
        surf.fill(self.__background_color)
        border_size = self.__dimen_border.size

        border_color = tools.shift_intensiveness(self.__background_color, -50)

        surf = tools.add_shadow(surf, border_color, border_size)

        return surf

    def get_logic_pos(self):
        """
        get the logic position of this view\n
        :return:
        """
        return self.__dimen.pos()

    def render(self):

        buf = self.get_gameobject()
        surf = self.__background_surface.copy()

        dimen = self.__dimen
        x = self.__dimen_padd.left

        for p in buf:
            idx = buf.index(p)
            pd_h = p.get_dimen().height
            y = self.__dimen_padd.top + ((self.__dimen.dist + pd_h) * idx)

            p.set_pos(dimen.x + x, dimen.y + y)

            p_view = PacketView(p)
            surf.blit(p_view.render(), (x, y))

        return surf


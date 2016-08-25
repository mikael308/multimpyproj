import src.resource.resource as resource
import pygame
from view_object import ViewObject
import src.output.view.tools as tools


class PacketView(ViewObject):
    """
    Represents a packet\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    # TEXT SURFACE
    __text_color = resource.get_color("packet_text").rgb()

    __border_color  = resource.get_color("packet_border").rgb()
    __background_color = resource.get_color("packet").rgb()

    __packet_padd_dimen = resource.get_dimen("packet_padd")
    __border_dimen = resource.get_dimen("packet_border")

    __separator     = None

    __packet = None

    def __init__(self, packet):
        """

        :param sender: sender adress
        :type sender: int
        :param receiver: receiver adress
        :type receiver: int
        :param checksum: checksum
        :type checksum: int
        """
        pygame.font.init()

        self.__packet = packet

        img = pygame.Surface(packet.get_dimen().wh())
        img.fill(self.__background_color)

        ViewObject.__init__(self, img, packet)

        self.__separator = pygame.Surface((self.__border_dimen.size, packet.get_dimen().height))
        self.__separator.fill(self.__border_color)

        self.__blit_adress()
        self.__blit_borders()

    def __blit_adress(self):
        """
        blit the adresses to the current image\n
        used as part of __init__\n
        :return: None
        """
        p = self.__packet

        adresses =  str(bin(p.get_sender())), \
                    str(bin(p.get_receiver())), \
                    str(bin(p.get_checksum()))
        self.__blit_content(adresses)

    def __blit_content(self, content):
        """
        blit content to this surface\n
        used as part of __init__
        :param content: the content to blit
        :return: None
        """
        font_res    = resource.get_font("packet")
        text        = pygame.font.SysFont(font_res.name, font_res.size)
        dimen       = self.__packet.get_dimen()
        img         = self.get_image()
        n_content   = len(content)
        padd_right  = self.__packet_padd_dimen.right

        # add shadow
        shadow_color = tools.shift_intensiveness(self.__background_color, -50)
        tools.add_shadow(img, shadow_color, 6)

        y = (dimen.height / 2) - (font_res.size / 2)  # center text
        for i, data in enumerate(content):
            text_surf = text.render(data, 0, self.__text_color)
            width = text.size(data)[0]
            idx = i + 1
            end_line = ((dimen.width / n_content) * idx)
            img.blit(self.__separator, (end_line, 0))

            x = end_line - width - padd_right
            img.blit(text_surf, (x, y))

    def __blit_borders(self):
        """
        blit borders to this image surface\n
        used as part of __init__\n
        :return: None
        """
        dimen           = self.__packet.get_dimen()
        img             = self.get_image()
        border_size     = self.__border_dimen.size
        border_color    = self.__border_color

        pygame.draw.lines(img, border_color, False,
                          ((0, 0),
                           (dimen.width-border_size, 0),
                           (dimen.width-border_size, dimen.height-border_size),
                           (0, dimen.height-border_size),
                           (0, 0)), border_size)

    def __str__(self):
        return str(self.__packet)



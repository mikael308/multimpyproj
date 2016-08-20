import src.resource.resource as resource
import pygame
from gameobject import GameObject


class Packet(GameObject):
    """
    define a packet holding a value\n

    :author: Mikael Holmbom
    :ver: 1.0
    """

    # TEXT SURFACE
    __text_color = 0, 0, 0  # black
    __text_size = 30

    __border_color  = resource.get_color("packet_border").rgb()

    __packet_padd_dimen = resource.get_dimen("packet_padd")
    __border_dimen = resource.get_dimen("packet_border")

    # this packet value
    __receiver      = 0
    __sender        = 0
    __checksum      = 0

    __separator     = None

    def __init__(self, sender, receiver, checksum):
        """

        :param sender:
        :type sender: int
        :param receiver:
        :type receiver: int
        :param checksum:
        :type checksum: int
        """
        dimen = resource.get_dimen("packet")
        src = resource.get_imagesrc("packet")
        img = pygame.image.load(src)

        text = pygame.font.SysFont("val_label", self.__text_size)
    def __blit_content(self, content):
	"""
	blit content to this surface\n
	used as part of __init__\n
	:param content: the content to blit
	:return: None
	"""
        font_res    = resource.get_font("packet")
        text        = pygame.font.SysFont(font_res.name, font_res.size)
        dimen       = self.get_dimen()
        img         = self.get_image()
        n_content   = len(content)
        padd_right  = self.__packet_padd_dimen.right

        GameObject.__init__(self, img, dimen)

        self.__sender = sender
        self.__receiver = receiver
        self.__checksum = checksum

        self.__separator = pygame.Surface((self.__border_dimen.size, dimen.height))
        self.__separator.fill(self.__border_color)


    def __blit_content(self, content):
	"""
	blit content to this surface\n
	used as part of __init__
	:param content: the content to blit
	:return: None
	"""
        font_res    = resource.get_font("packet")
        text        = pygame.font.SysFont(font_res.name, font_res.size)
        dimen       = self.get_dimen()
        img         = self.get_image()
        n_content   = len(content)
        padd_right  = self.__packet_padd_dimen.right

        y = (dimen.height / 2) - (font_res.size / 2)  # set to mid
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
        dimen           = self.get_dimen()
        img             = self.get_image()
        border_size     = self.__border_dimen.size
        border_color    = self.__border_color
        border_vert = pygame.Surface((border_size, dimen.height))
        border_hori = pygame.Surface((dimen.width, border_size))
        border_vert.fill(border_color)
        border_hori.fill(border_color)

        pygame.draw.lines(img, border_color, False,
                          ((0, 0),
                           (dimen.width-border_size, 0),
                           (dimen.width-border_size, dimen.height-border_size),
                           (0, dimen.height-border_size),
                           (0, 0)), border_size)

    def __str__(self):
        return "[ sender:" + str(self.get_sender()) + " | " + "receiver:" + str(self.get_receiver()) + " | " + "checksum:" + str(self.get_checksum()) + " ]"

    def get_checksum(self):
        """
        get this checksum value\n
        :return:
        """
        return self.__checksum

    def get_sender(self):
        """
        get this sender value\n
        :return:
        """
        return self.__sender

    def get_receiver(self):
        """
        get this receiver value\n
        :return: this value
        """
        return self.__receiver

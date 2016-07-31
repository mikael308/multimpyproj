import resource, pygame
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

    # this packet value
    __val = 0

    def __init__(self, val):
        src = resource.get_imagesrc("packet")
        img = pygame.image.load(src)

        text = pygame.font.SysFont("val_label", self.__text_size)
        text_val = str(bin(val))

        img.blit(text.render(text_val, 0, self.__text_color), (120, 5))
        GameObject.__init__(self, img)

        self.__val = val

    def get_val(self):
        """
        get this value
        :return: this packet value
        """
        return self.__val

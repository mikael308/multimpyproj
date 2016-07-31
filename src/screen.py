import resource, pygame
from infopanel import InfoPanel


class Screen:
    """
    
    :author: Mikael Holmbom
    :ver: 1.0
    """

    __main_surface  = None
    __infopanel     = None

    __player        = None
    __cpus          = None
    __packets       = None

    __background    = None

    def __init__(self, size, player, cpus, packets):
        self.__main_surface     = pygame.display.set_mode(size)
        self.__player           = player
        self.__cpus             = cpus
        self.__packets          = packets

        self.__infopanel = InfoPanel(player)

        self.__background = pygame.image.load(resource.get_imagesrc("background"))

    def __blit(self, obj):
        """
        displays object on current screen
        :param object: object to display
        :return:
        """
        self.__main_surface.blit(obj.get_sprite(), obj.get_rect())

    def render(self):
        """
        display all current objects on current screen
        :return:
        """
        self.__main_surface.blit(self.__background, (0, 0))

        for i in self.__cpus:
            self.__blit(i)

        for p in self.__packets.values():
            self.__blit(p)

        self.__blit(self.__player)

        self.__main_surface.blit(self.__infopanel.render(), (10, 10))

        pygame.display.update()

    def get_width(self):
        """
        return the screens width
        :return:
        """
        return self.__main_surface.get_width()

    def get_height(self):
        """
        returns the screens height
        :return:
        """
        return self.__main_surface.get_height()

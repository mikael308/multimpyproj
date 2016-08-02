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
    __buf           = None
    __cpus          = None
    __packets       = None

    __background    = pygame.image.load(resource.get_imagesrc("background"))

    __buf_margin_left       = resource.get_dimen("buf_margin_left")
    __buf_margin_top        = resource.get_dimen("buf_margin_top")
    __buf_margin_dist       = resource.get_dimen("buf_margin_dist")

    __cpu_margin_left       = resource.get_dimen("cpu_margin_left")
    __cpu_margin_top        = resource.get_dimen("cpu_margin_top")
    __cpu_margin_dist       = resource.get_dimen("cpu_margin_dist")

    def __init__(self, size):
        self.__main_surface     = pygame.display.set_mode(size)

    def set_cpus(self, cpus):
        """
        set this pointer to cpus to display
        :param cpus:
        :return:
        """
        self.__cpus = cpus
        return self



    def __blit(self, obj):
        """
        displays object on current screen
        :param object: object to display
        :return:
        """
        self.__main_surface.blit(obj.get_sprite(), obj.get_rect())

    def update(self):
        """
        update the objects displayed on screens
        :return:
        """
        x = self.__buf_margin_left
        for p in self.__buf:

            idx = self.__buf.index(p)
            y = self.__buf_margin_bottom - (self.__buf_margin_dist * idx)
            p.set_pos(x, y)

    def render(self):
        """
        display all current objects on current screen
        :return:
        """
        self.__main_surface.blit(self.__background, (0, 0))

        for i in self.__cpus:
            self.__blit(i)

        for p in self.__packets:
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


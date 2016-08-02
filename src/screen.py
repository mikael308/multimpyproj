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

    __buffer_background = None

    __background    = pygame.image.load(resource.get_imagesrc("background"))

    __buf_margin_left       = resource.get_dimen("buf_margin_left")
    __buf_margin_top        = resource.get_dimen("buf_margin_top")
    __buf_margin_dist       = resource.get_dimen("buf_margin_dist")

    __buf_background_x      = __buf_margin_left - resource.get_dimen("buf_margin_background_w")
    __buf_background_y      = __buf_margin_top - resource.get_dimen("buf_margin_background_h")

    __cpu_margin_left       = resource.get_dimen("cpu_margin_left")
    __cpu_margin_top        = resource.get_dimen("cpu_margin_top")
    __cpu_margin_dist       = resource.get_dimen("cpu_margin_dist")

    def __init__(self, size):
        self.__main_surface     = pygame.display.set_mode(size)

    def set_player(self, player):
        """
        set this pointer to player to display
        :param player:
        :type player: Player
        :return:
        """
        self.__player = player
        return self

    def set_buffer(self, buffer):
        """
        set this pointer to buffer to display
        :param buffer:
        :type buffer: Buffer
        :return:
        """
        self.__buf = buffer
        return self

    def set_cpus(self, cpus):
        """
        set this pointer to cpus to display
        :param cpus:
        :type cpus: CPU
        :return:
        """
        self.__cpus = cpus
        return self

    def set_packets(self, packets):
        """
        set this pointer to packets to display
        :param packets:
        :type packets: Packet
        :return:
        """
        self.__packets = packets
        return self

    def setup(self):
        """
        initialize values for all the objects in this screen
        :return:
        """
        buf_bg_w = 250
        buf_bg_h = (self.__buf_margin_dist * resource.get_value("buf_capacity")) + (2 * resource.get_dimen("buf_margin_background_h"))

        self.__buffer_background = pygame.Surface((buf_bg_w, buf_bg_h))
        self.__buffer_background.fill((230, 0, 0))

        if self.__player:
            self.__infopanel = InfoPanel(self.__player)

        for i in range(0, len(self.__cpus)):
            x = self.__cpu_margin_left
            y = self.__cpu_margin_top + self.__cpu_margin_dist * i
            self.__cpus[i].set_pos(x, y)

        self.update()

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
            y = self.__buf_margin_top + (self.__buf_margin_dist * idx)
            p.set_pos(x, y)

    def render(self):
        """
        display all current objects on current screen
        :return:
        """
        self.__main_surface.blit(self.__background, (0, 0))


        self.__main_surface.blit(self.__buffer_background, (self.__buf_background_x, self.__buf_background_y))

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


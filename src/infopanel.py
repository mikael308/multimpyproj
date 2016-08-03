import pygame, resource


class InfoPanel:
    """
    panel displaying information about player

    :author: Mikael Holmbom
    :ver: 1.0
    """

    """ this player to display in panel    """
    __player        = None
    """ icons representing health points """
    __health_icon   = None

    __text_size     = 0
    __text_color    = (0, 0, 0)
    __startpoint    = resource.get_dimen("infopanel_x"), resource.get_dimen("infopanel_y")

    def __init__(self, player,text_size=40, text_color=(0, 0, 0)):
        self.__player = player

        src = resource.get_imagesrc("health")
        self.__health_icon = pygame.image.load(src)
        self.__text_size    = text_size
        self.__text_color   = text_color

    def render(self):
        """
        render this panel
        :return: surface instance of this infopanel
        """
        panel = pygame.Surface((200, 50), pygame.SRCALPHA, 32)
        panel.convert_alpha(panel)
        panel.convert_alpha(panel)

        w = self.__startpoint[0]
        for i in range(0, self.__player.get_health()):
            panel.blit(self.__health_icon, (w, self.__startpoint[1]))
            w += 30

        text_size = 40
        text_color = 0, 0, 0
        text = pygame.font.SysFont("player_score_label", text_size)
        text_val = str(self.__player.get_score())

        if w < self.__startpoint[0] + 90:
            w = self.__startpoint[0] + 90

        panel.blit(text.render(text_val, 0, text_color), (w, self.__startpoint[1]))

        return panel


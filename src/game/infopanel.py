import pygame
import src.resource as resource


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

    def __init__(self, text_size=resource.get_dimen("infopanel_textsize"), text_color=(0, 0, 0)):

        src = resource.get_imagesrc("health")
        self.__health_icon = pygame.image.load(src)
        self.__text_size    = text_size
        self.__text_color   = text_color

    def set_player(self, player):
	"""
	set this player as source of panels data to output
	:return: this InfoPanel
	"""
        self.__player = player
	return self

    def render(self):
        """
        render this panel
        :return: surface instance of this infopanel
        """
        panel = pygame.Surface((200, 50), pygame.SRCALPHA, 32)
        panel.convert_alpha(panel)

        y = self.__startpoint[1]
        x = self.__startpoint[0]
        for i in range(0, self.__player.get_health()):
            panel.blit(self.__health_icon, (x, self.__startpoint[1]))
            x += 30

        text_color = 0, 0, 0
        text = pygame.font.SysFont("player_score_label", self.__text_size)
        text_val = str(self.__player.get_score())

        # SCORE
        ######################
        if x < self.__startpoint[0] + 90:
            x = self.__startpoint[0] + 90

        panel.blit(text.render(text_val, 0, text_color), (x, y))

        # LEVEL
        ######################
        x += 50
        text_val = str(self.__player.get_level())
        panel.blit(text.render(text_val, 0, text_color), (x, y))

        return panel


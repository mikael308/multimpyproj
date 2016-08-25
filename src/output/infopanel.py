import pygame
import src.resource.resource as resource
import src.output.view.tools as viewtools
from view_object import ViewObject


class InfoPanel(ViewObject):
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

    def __create_background(self):
	"""
        create a background for this infopanel
        :return:
        """
        surf = pygame.Surface(self.__dimen.wh())
        surf.fill(self.__background_color)
        border_size = resource.get_dimen("infopanel_border").size
        col_diff = -50
        bbc = []
        for v in self.__background_color:
            c = v + col_diff
            if c < 0:
                c = 0
            elif c > 255:
                c = 255
            bbc.append(c)

        border_color = bbc[0], bbc[1], bbc[2]

        surf = viewtools.add_shadow(surf, border_color, border_size)

        return surf

        self.__player = player
	return self

    def render(self):
        """
        render this panel
        :return: surface instance of this infopanel
        """
        panel = pygame.Surface((200, 50), pygame.SRCALPHA, 32)
        panel.convert_alpha(panel)
        if self.__player is None:
        	return panel

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


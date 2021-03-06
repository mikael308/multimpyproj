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
    __n_health_start = resource.get_value("player_hp_start")

    __dimen = resource.get_dimen("infopanel")
    __dimen_health  = resource.get_dimen("infopanel_health")

    __font_res      = resource.get_font("infopanel")
    __text_color    = resource.get_color("infopanel_text").rgb()

    __background_color = resource.get_color("infopanel_background").rgb()
    __background_surf = None

    def __init__(self):

        src = resource.get_imagesrc("health")
        self.__health_icon  = pygame.image.load(src)
        self.__health_icon  = pygame.transform.scale(self.__health_icon, (self.__dimen_health.wh()))
        self.__text         = pygame.font.SysFont(self.__font_res.name, self.__font_res.size)
        self.__background_surf = self.__create_background()

        ViewObject.__init__(self, self.__background_surf)

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

    def set_player(self, player):
        """
        set this player as source of panels data to view
        :return: this InfoPanel
        """
        self.__player = player
        return self

    def render(self):
        """
        render this panel
        :return: surface instance of this infopanel
        """
        panel_surf = self.__background_surf.copy()

        if self.__player is None:
            return panel_surf

        dimen = self.__dimen
        x = dimen.x
        y = dimen.y

        # HEALTH
        #####################
        for i in range(0, self.__player.get_health()):
            panel_surf.blit(self.__health_icon, (x, dimen.y))
            x += self.__dimen_health.width + self.__dimen_health.dist

        x = ((self.__dimen_health.width + self.__dimen_health.dist ) * self.__n_health_start) + dimen.dist

        # SCORE
        ######################
        text_val = str(self.__player.get_score())

        panel_surf.blit(self.__text.render(text_val, 0, self.__text_color), (x, y))

        # LEVEL
        ######################
        x += self.__dimen.dist * 2
        text_val = str(self.__player.get_level())
        panel_surf.blit(self.__text.render(text_val, 0, self.__text_color), (x, y))

        return panel_surf

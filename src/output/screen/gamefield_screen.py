import pygame

import src.resource.resource as resource
from src.output.screen.screen import Screen
from src.output.view.buffer_view import BufferView
from src.output.view.gameobjects.gameobject import GameObject


class GameFieldScreen(Screen):
    """
    Screen used to view the gameplay\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    __buffer_background     = None
    #__buf_background_color  = resource.get_color("game_buffer_background").rgb()
    #__buf_border_dimen      = resource.get_dimen("game_buffer_border")

    #__buf_dimen             = resource.get_dimen("game_buffer_background")
    #__buf_padd              = resource.get_dimen("game_buffer_background_padd")

    __scaling_factor_x      = 0
    __scaling_factor_y      = 0

    __gameengine            = None

    def __init__(self, dimen=resource.get_dimen("gamefieldscreen")):
        Screen.__init__(self, dimen, False)

        self.__dimen = dimen




    def set_gameengine(self, gameengine):
        """
        set a gameengine to get all viewing objects from\n
        :param gameengine:
        :return:
        """
        self.__gameengine = gameengine
        self.__buffer_background = BufferView(self.__gameengine.get_buffer())

    def get_scaling_factors(self):
        """
        get the scaling factors of this screen\n
        :return:
        """
        return self.__scaling_factor_x, self.__scaling_factor_y

    def setup(self):
        Screen.setup(self)

        gs_w = self.get_dimen().width
        gs_h = self.get_dimen().height

        gamefield_dimen = resource.get_dimen("gamefield")
        gf_w = gamefield_dimen.width
        gf_h = gamefield_dimen.height

        self.__scaling_factor_x = gs_w / (gf_w + 0.0)
        self.__scaling_factor_y = gs_h / (gf_h + 0.0)

        self._get_background().fill(resource.get_color("gamefield_background").rgb())

        bg = self._get_background()

        if self.__gameengine is not None:
            n_cpus = len(self.__gameengine.get_cpus())
            cpu_dimen = resource.get_dimen("cpu")
            top = (self.get_dimen().height / 2) - ((n_cpus * cpu_dimen.diameter()) - (n_cpus * cpu_dimen.dist))
            top /= 2

            for idx, cpu in enumerate(self.__gameengine.get_cpus()):
                x = cpu.get_dimen().left
                y = (top + cpu.get_dimen().dist * idx)

                cpu.set_pos(x, y)

        self.update()

    def _scale_to_screen(self, (x, y)):
        """
        scale position coordinates to adjust to gamefield screen size\n
        :return:
        """
        x *= self.__scaling_factor_x
        y *= self.__scaling_factor_y

        return x, y

    def _scale_surface_to_screen(self, surf):
        """
        scale surface to adjust to gamefield screen size\n
        :param surf:
        :return:
        """
        old_w = int(surf.get_width())
        old_h = int(surf.get_height())

        w, h = self._scale_to_screen((old_w, old_h))

        return pygame.transform.scale(surf, (int(w), int(h)))

    def _blit(self, object, pos=None):
        """
        blit object mainsurface\n
        :param object: the object to blit
        :param pos: position of object
        :return:
        """
        x = 0
        y = 0
        if pos is not None:
            x += pos[0]
            y += pos[1]
        else:
            if isinstance(object, GameObject):
                x += object.get_pos()[0]
                y += object.get_pos()[1]

        x, y = self._scale_to_screen((x, y))

        surf = None
        if isinstance(object, GameObject):
            surf = object.get_image()
        else:
            surf = object
        scaled_img = self._scale_surface_to_screen(surf)

        self._get_main_surface().blit(scaled_img, (x, y))

    def update(self):
        """
        updates the objects\n
        :return:
        """
        pass

    def render(self):
        """

        :return:
        """
        Screen.render(self)

        #self._get_main_surface().blit(self.__buffer_background.render(), (50,50)) #TODO denna ar tmp
        self._blit(self.__buffer_background.render(), (50,50)) #TODO denna ar tmp

        for cpu in self.__gameengine.get_cpus():
            self._blit(cpu)

        self._blit(self.__gameengine.get_trash())

        for p in self.__gameengine.get_packets():
            self._blit(p)

        self._blit(self.__gameengine.get_player())

        return self._get_main_surface()

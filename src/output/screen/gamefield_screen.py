import pygame
import src.resource.resource as resource
from src.output.screen.screen import Screen
from src.output.view.view_object import ViewObject
from src.output.view.buffer_view import BufferView
from src.output.view.player_view import PlayerView
from src.output.view.packet_view import PacketView
from src.output.view.trash_view import TrashView
from src.output.view.cpu_view import CPUView


class GameFieldScreen(Screen):
    """
    Screen used to view the gameplay\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    __scaling_factor_x      = 0
    __scaling_factor_y      = 0

    __game_controller       = None

    # VIEW_OBJECTS
    __buffer_view           = None
    __buffer_packets        = []
    __cpu_views             = []
    __packet_views          = []
    __player_view           = None
    __trash_view            = None

    def __init__(self, dimen=resource.get_dimen("gamefieldscreen")):
        Screen.__init__(self, dimen, False)

        self.__dimen = dimen

    def set_game_controller(self, gamecontroller):
        """
        set a game_controller to get all viewing objects from\n
        :param gamecontroller:
        :return:
        """
        self.__game_controller = gamecontroller

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

        self.__buffer_view = BufferView(self.__game_controller.get_buffer())

        if self.__game_controller is not None:
            gc = self.__game_controller
            # PLAYER
            self.__player_view = PlayerView(gc.get_player())

            # CPU
            n_cpus = len(gc.get_cpus())
            cpu_dimen = resource.get_dimen("cpu")
            top = (self.get_dimen().height / 2) - ((n_cpus * cpu_dimen.diameter()) - (n_cpus * cpu_dimen.dist))
            top /= 2

            for idx, cpu in enumerate(gc.get_cpus()):
                x = cpu.get_dimen().left
                y = (top + cpu.get_dimen().dist * idx)

                cpu.set_pos(x, y)
                cpu_view = CPUView(cpu)

                self.__cpu_views.append(cpu_view)

            # PACKET
            for packet in gc.get_packets():
                idx = gc.get_buffer().index(packet)

                self.__packet_views.append(PacketView(packet))

            self.__trash_view = TrashView(gc.get_trash())

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
            if isinstance(object, ViewObject):
                if object.has_gameobject():
                    x += object.get_logic_pos()[0]
                    y += object.get_logic_pos()[1]
                else:
                    x += object.get_pos()[0]
                    y += object.get_pos()[1]

        x, y = self._scale_to_screen((x, y))

        surf = None
        if isinstance(object, ViewObject):
            surf = object.render()
        elif isinstance(object, pygame.Surface):
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

        self._blit(self.__buffer_view)

        for cpu in self.__cpu_views:
            self._blit(cpu)

        self._blit(self.__trash_view)

        for p in self.__game_controller.get_pending_packets():
            pv = PacketView(p)
            self._blit(pv)

        self._blit(self.__player_view)

        return self._get_main_surface()


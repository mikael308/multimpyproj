import pygame
import src.settings.game_controls as game_controls
import src.settings.navigation_controls as nav_controls
import src.settings.settings_controls as settings_controls
import src.settings.settings as settings
from src.event.eventhandler import EventHandler


class GameEventHandler(EventHandler):
    """
    Handling events from use-case: Game\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    __game_time     = None
    __game_clock    = None

    def __init__(self, interface):
        EventHandler.__init__(self, interface)
        self.__game_time = 0
        self.__game_clock = pygame.time.Clock()
        pygame.key.set_repeat(10, 10)

    def handle(self, event):
        intf = self._get_interface()

        if event.type == pygame.QUIT:
            if intf is not None:
                intf.shutdown()
                intf.close()
                pygame.quit()

        if event.type == pygame.MOUSEBUTTONUP:
            output = intf.get_output()
            pos = pygame.mouse.get_pos()

            output.get_screen().click(pos)

        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()

            if key[nav_controls.key_quit]:
                intf.shutdown()

            elif key[nav_controls.key_back]:
                intf = self._get_interface()
                intf.back()

            else:
                ## MOVEMENT
                mov = self._parse_movement_event(key)
                intf.get_controller().mov_player(mov)

        elif event.type == pygame.KEYUP:
            key = event.key

            ###############################################
            # DEBUG
            if pygame.key.get_mods() & pygame.KMOD_ALT:
                if key == pygame.K_s:
                    intf.get_controller().score()
                    intf.get_output().score()

                elif key == pygame.K_a:
                    intf.get_controller().add_packet()
                    intf.get_output().update()
                elif key == pygame.K_k:
                    intf.get_controller().get_player().mod_health(-1)

                elif key == pygame.K_p:
                    for p in self._get_interface().get_controller().get_packets():
                        print " * " + str(p.get_receiver())
            # ! DEBUG
            ####################################################
            if key == settings_controls.key_switch_sound_enabled:
                intf.get_output().switch_sound_enabled()

            elif key == game_controls.key_action:
                e = intf.get_controller()
                player = e.get_player()

                if player.has_attached():
                    # DETACH PACKET
                    rp_res = e.release_packet()
                    if rp_res == 1:
                        intf.get_output().score()
                    elif rp_res == -1:
                        intf.get_output().wrong_cpu()

                else:
                    # ATTACH PACKET
                    plr = player.get_rect()
                    for p in e.get_packets():
                        pr = p.get_rect()
                        if pr.colliderect(plr):
                            e.grab_packet(p)

    @staticmethod
    def __slow_key():
        pygame.key.set_repeat(1000, 1000)

    def repeated_tasks(self):
        """
        gamelogic tasks not triggered by user input\n
        :return:
        """

        # delay framerate
        self.__game_time += self.__game_clock.tick(settings.get_FPS())

        i = self._get_interface()
        out     = i.get_output()
        e       = i.get_controller()
        player = e.get_player()
        while player.get_score() >= e.get_points_to_next_level():
            e.level_up()
            out.level_up()

        # spawn new packets every x second
        if self.__game_time % e.get_timespan_add_packet() < settings.get_holdtime():
            if e.add_packet():
                out.update()
            else:
                out.buffer_overflow()

        if not player.is_alive():
            e.shutdown()

    @staticmethod
    def _parse_movement_event(key):
        """
        parses key event as movement\n
        :Example: if the returned tuple[0] is positive, this movement is a positive movement on the x-axis\n
        :param key: the pressed key
        :type key: pygame.key
        :return: movement as tuple (x_movement, y_movement)
        :returns: tuple
        """
        ddir = 0.7  # diagonal direction: factor multiplied to distance on diagonal movement

        left    = game_controls.key_mov_left
        right   = game_controls.key_mov_right
        up      = game_controls.key_mov_up
        down    = game_controls.key_mov_down

        def get_mov(key, neg_dir, pos_dir):
            """
            inner function;\n
            determine if key pressed compares with the negative or positive key-value according to wanted axis\n
            if no movement was found, 0 is returned\n
            :Example: in X-axis -> neg_dir=left, pos_dir=right\n
            :param key: pressed key
            :param neg_dir: key that generates negative values
            :param pos_dir: key that generates positive values
            :return: movement in one axis
            """
            if key[neg_dir]:
                return -1.0
            elif key[pos_dir]:
                return 1.0
            else:
                return 0

        mov_x = get_mov(key, left, right)
        mov_y = get_mov(key, up, down)

        if mov_x is not 0 and mov_y is not 0:
            # if diagonally movement
            mov_x *= ddir
            mov_y *= ddir

        return mov_x, mov_y

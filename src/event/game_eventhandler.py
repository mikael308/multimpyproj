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

    def __init__(self):
        EventHandler.__init__(self)
        self.__game_time = 0
        self.__game_clock = pygame.time.Clock()
        pygame.key.set_repeat(10, 10)

    def handle(self, event):
        EventHandler.handle(self, event)

        controller = self.get_controller()

        if event.type == pygame.QUIT:
            controller.shutdown()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            output = controller.get_output()
            output.click(pos)

        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()

            if key[nav_controls.key_quit]:
                controller.shutdown()

            elif key[nav_controls.key_back]:
                controller.stop()

            else:
                ## MOVEMENT
                mov = self._parse_movement_event(key)
                controller.mov_player(mov)

        elif event.type == pygame.KEYUP:
            key = event.key

            ###############################################
            # DEBUG
            if pygame.key.get_mods() & pygame.KMOD_ALT:
                if key == pygame.K_s:
                    controller.score()

                elif key == pygame.K_a:
                    controller.add_packet()

                elif key == pygame.K_k:
                    controller.damage_player()


                elif key == pygame.K_i:
                    print "PENDING PACKETS"
                    for p in intf.get_controller().get_pending_packets():
                        print " - " + str(p.get_pos()) + "  " + str(p)
                    print "BUFFER PACKETS"
                    buf = intf.get_controller().get_buffer()
                    for p in buf:
                        print " ["+str(buf.index(p)) +"] "+str(p.get_pos())+" " + str(p)
            # ! DEBUG
            ####################################################
            if key == settings_controls.key_switch_sound_enabled:
                controller.switch_soundfx_enabled()

            elif key == game_controls.key_pickup:
                player = controller.get_player()

                if player.has_attached():
                    # DETACH PACKET
                    controller.release_packet()

                else:
                    # ATTACH PACKET
                    plr = player.get_rect()
                    for p in controller.get_packets():
                        pr = p.get_rect()
                        if pr.colliderect(plr):
                            controller.grab_packet(p)
                            break

    def repeated_tasks(self):
        """
        gamelogic tasks not triggered by user input\n
        :return:
        """

        # delay framerate
        self.__game_time += self.__game_clock.tick(settings.get_FPS())

        controller       = self.get_controller()
        out     = controller.get_output()
        player = controller.get_player()

        # player level up
        while player.get_score() >= controller.get_points_to_next_level():
            controller.level_up()
            out.level_up()

        # spawn new packets every x second
        if self.__game_time % controller.get_timespan_add_packet() < settings.get_holdtime():
            controller.add_packet()

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

    def _print_packets(self):
        """
        debug function\n
        prints out all current packets in pending state and contained in buffer\n
        :return:
        """
        controller = self.get_controller()
        print "PENDING PACKETS"
        for p in controller.get_pending_packets():
            print " - " + str(p.get_pos()) + "  " + str(p)
        print "BUFFER PACKETS"
        buf = controller.get_buffer()
        for p in buf:
            print " [" + str(buf.index(p)) + "] " + str(p.get_pos()) + " " + str(p)


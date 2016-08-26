import pygame
import src.settings.navigation_controls as nav_controls
from eventhandler import EventHandler


class ResultEventHandler(EventHandler):
    """
    eventhandler for use-case: result\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def handle(self, event):
        EventHandler.handle(self, event)
        controller = self.get_controller()

        if event.type == pygame.QUIT:
            controller.shutdown()

        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()

            if key[nav_controls.key_quit]:
                controller.shutdown()

            elif key[nav_controls.key_back]:
                controller.stop()

            controller.stop()


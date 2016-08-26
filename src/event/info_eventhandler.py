import pygame
import src.settings.navigation_controls as nav_controls
from eventhandler import EventHandler


class InfoEventHandler(EventHandler):
    """
    eventhandler for use-case: Info\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def handle(self, event):

        if event.type == pygame.QUIT:
            self.get_controller().shutdown()

        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()

            if key[nav_controls.key_quit]:
                self.get_controller().shutdown()
            elif key[nav_controls.key_back]:
                self.get_controller().stop()


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
        interf = self._get_interface()

        if event.type == pygame.QUIT:
            if interf is not None:
                interf.get_controller().shutdown()
                pygame.quit()

        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()

            if key[nav_controls.key_quit]:
                interf.get_controller().shutdown()
                pygame.quit()

            elif key[nav_controls.key_back]:
                interf.get_controller().shutdown()

            interf.get_controller().shutdown()


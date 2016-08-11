import pygame
import src.settings.controls as controls
from eventhandler import EventHandler


class InfoEventHandler(EventHandler):
    """
    eventhandler for use-case: Info\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def handle(self, event):
        interf = self._get_interface()

        if event.type == pygame.QUIT:
            if interf is not None:
                interf.shutdown()
                pygame.quit()

        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()

            if key[controls.key_quit]:
                interf.shutdown()
            elif key[controls.key_back]:
                interf.shutdown()


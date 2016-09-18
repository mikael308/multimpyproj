import pygame
import src.settings.navigation_controls as controls
from eventhandler import EventHandler


class StartMenuEventHandler(EventHandler):
    """
    eventhandler for use-case: Startmenu\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def handle(self, event):
        EventHandler.handle(self, event)

        controller = self.get_controller()

        if event.type == pygame.QUIT:
            if controller is not None:
                controller.shutdown()
                pygame.quit()

        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()

            if key[controls.key_quit]:
                controller.shutdown()
                self.stop()

            elif key[pygame.K_ESCAPE]:
                controller.shutdown()
                self.stop()

            elif pygame.key.get_mods() & pygame.KMOD_ALT:
                if key[pygame.K_s]:
                    controller.get_output().get_btns()["START"].click()

                elif key[pygame.K_i]:
                    controller.get_output().get_btns()["INFO"].click()

                elif key[pygame.K_e]:
                    controller.get_output().get_btns()["EXIT"].click()

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            controller.get_output().click(pos)

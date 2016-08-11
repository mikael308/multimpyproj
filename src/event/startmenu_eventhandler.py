import pygame
import src.settings.controls as controls
from eventhandler import EventHandler


class StartMenuEventHandler(EventHandler):
    """
    eventhandler for use-case: Startmenu\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def handle(self, event):
        interf = self._get_interface()

        if event.type == pygame.QUIT:
            if interf is not None:
                interf.get_engine().shutdown()
                pygame.quit()

        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()

            if key[controls.key_quit]:
                interf.get_engine().shutdown()

            elif key[pygame.K_ESCAPE]:
                interf.get_engine().shutdown()

            elif key[pygame.K_s]:
                for b in interf.get_output().get_btns():
                    if b.get_id() == "START":
                        b.click()
            elif key[pygame.K_i]:
                for b in interf.get_output().get_btns():
                   if b.get_id() == "INFO":
                        b.click()
            elif key[pygame.K_e]:
                for b in interf.get_output().get_btns():
                    if b.get_id() == "EXIT":
                        b.click()

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            for b in interf.get_output().get_btns().itervalues():
                if b.get_rect().collidepoint(pos):
                    b.click()
                    break
import pygame
import src.resource.resource as resource
from src.settings import settings


class SoundController:
    """
    facade controlling sounds\n
    reads soundfiles from resourcefile: sounds.xml\n
        * use play(self, id) to play sound with id as matching attribute name from resource item
        * close() to release resource\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    # dictionary of sounds from resource file
    __sounds = {}

    def __init__(self):
        pygame.mixer.init()

        res = resource.get_all_soundsrc()

        for name, soundsrc in res.iteritems():
            self.__sounds[name] = pygame.mixer.Sound(soundsrc)

    def close(self):
        """
        close this and release resources
        :return: None
        """
        pygame.mixer.quit()

    def play(self, id):
        """
        play sound of id param\n
        id must match with attrib name in resource item in resource file\n
        settings soundfx must be enabled to successfully play
        :param id:
        :type id: string
        :return: None
        """
        if settings.is_soundfx_enabled():
            self.__sounds[id].play()

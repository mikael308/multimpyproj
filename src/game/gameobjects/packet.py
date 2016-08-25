import src.resource.resource as resource
import pygame
from game_object import GameObject


class Packet(GameObject):
    """
    define a packet holding a value\n

    :author: Mikael Holmbom
    :ver: 1.0
    """

    # this packet value
    __receiver      = 0
    __sender        = 0
    __checksum      = 0

    __separator     = None

    def __init__(self, sender, receiver, checksum):
        """

        :param sender:
        :type sender: int
        :param receiver:
        :type receiver: int
        :param checksum:
        :type checksum: int
        """
        dimen = resource.get_dimen("packet")

        rect = pygame.Rect((0, 0), dimen.wh())

        GameObject.__init__(self, dimen, rect)

        self.__sender = sender
        self.__receiver = receiver
        self.__checksum = checksum

    def __str__(self):
        return "[ sender:" + str(self.get_sender()) + " | " + "receiver:" + str(self.get_receiver()) + " | " + "checksum:" + str(self.get_checksum()) + " ]"

    def get_checksum(self):
        """
        get this checksum value\n
        :return:
        """
        return self.__checksum

    def get_sender(self):
        """
        get this sender value\n
        :return:
        """
        return self.__sender

    def get_receiver(self):
        """
        get this receiver value\n
        :return: this value
        """
        return self.__receiver

    def valid_checksum(self):
        """
        determine if this checksum is valid as: checksum = receiver AND sender\n
        :return: True if checksum is valid
        """
        return self.get_checksum() == self.get_receiver() & self.get_sender()


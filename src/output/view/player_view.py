import pygame
import src.resource.resource as resource
from view_object import ViewObject


class PlayerView(ViewObject):
	"""
	Represents the player\n

	:author: Mikael Holmbom
	:version: 1.0
	"""

	def __init__(self, player):
		"""

		:param player:
		 :type player: src.game.gameobjects.Player
		"""
		self.__player = player

		img = pygame.Surface(player.get_dimen().wh())
		color = resource.get_color("player")
		img.fill(color.rgb())

		ViewObject.__init__(self, img, player)



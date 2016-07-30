import resource, pygame
from Attachable import Attachable


class Player(Attachable):
	"""
		defines the player

		author Mikael Holmbom
		ver 1.0
	"""

	# name of this player
	__name 		= ""
	# this current health value
	__health 	= 0
	# defines this movement speed
	__speed		= 0
	# this current score
	__score 	= 0

	def __init__(self, name, health, speed):
		src = resource.get_imagesrc("player")
		img 	= pygame.image.load(src)
		Attachable.__init__(self, img)

		self.__name 	= name
		self.__health 	= health
		self.__speed	= speed

	def set_health(self, health):
		"""
		set current health
		"""
		self.__health = health

	def set_speed(self, speed):
		"""
		set this speed value
		"""
		self.__speed = speed

	def get_name(self):
		"""
		get this name
		"""
		return self.__name

	def get_health(self):
		"""
		get current health
		"""
		return self.__health

	def get_speed(self):
		"""
		get current speed
		"""
		return self.__speed

	def is_alive(self):
		"""
		determines if this instance is alive
		"""
		return self.__health > 0

	def damage(self, damage):
		"""
		damage this player by param value
		:param damage: value to damage this player
		:return:
		"""
		hp = self.get_health()
		self.set_health(hp - damage)


import resource, pygame
from attachable import Attachable


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

	def set_score(self, score):
		"""
		set this score
		:param score: new score value
		:return:
		"""
		self.__score = score

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

	def get_score(self):
		"""
		get this current score
		:return:
		"""
		return self.__score

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

	def mod_score(self, diff):
		"""
		modify current score\n
		:param diff: modifying term\n
		increase score: positive integer param\n
		decrease score: negative integer param
		:return:
		"""
		s = self.get_score()
		self.set_score(s + diff)

import src.resource as resource
import pygame
from attachable import Attachable
from gameobject import GameObject


class Player(GameObject, Attachable):
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
	# this current level
	__level		= 0

	def __init__(self, name, health, speed):
		src = resource.get_imagesrc("player")
		img 	= pygame.image.load(src)
		GameObject.__init__(self, img)

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

	def set_level(self, level):
		"""
		set this level
		:param level:  new level value
		:return:
		"""
		self.__level = level

	def get_name(self):
		"""
		get this name
		:return: name attr
		"""
		return self.__name

	def get_health(self):
		"""
		get current health
		:return: health attr
		"""
		return self.__health

	def get_speed(self):
		"""
		get current speed
		:return: speed attr
		"""
		return self.__speed

	def get_score(self):
		"""
		get this current score
		:return:
		"""
		return self.__score

	def get_level(self):
		"""
		get this current level
		:return: this level
		"""
		return self.__level

	def is_alive(self):
		"""
		determines if this instance is alive
		:return: True if players health is > 0
		"""
		return self.__health > 0

	def move_pos(self, x, y):
		"""
		move current position\n
		:param x: X-axis direction\n
		:type x: int
		:param y: Y-axis direction\n
		:type y: int
		:return: None
		"""
		GameObject.move_pos(self, x, y)
		Attachable.move_pos(self, x, y)


	def damage(self, damage):
		"""
		damage this player by param value
		:param damage: value to damage this player
		:return:
		"""
		h = self.get_health()
		self.set_health(h - damage)

	def mod_score(self, diff):
		"""
		modify current score\n
		:param diff: modifying term: increase score: positive integer param, decrease score: negative integer param\n
		:type diff: int
		:return: score value after modification
		"""
		s = self.get_score()
		self.set_score(s + diff)
		return self.__score

	def mod_level(self, diff):
		"""
		modify current level\n
		:param diff: modifying term: increase level: positive integer param: decrease level: negative integer param
		:type diff: int
		:return:
		"""
		self.__level += diff

import src.resource.resource as resource
import pygame
from attachable import Attachable
from game_object import GameObject


class Player(GameObject, Attachable):
	"""
	defines the player of the game\n

	:author: Mikael Holmbom
	:version: 1.0
	"""

	# this current health value
	__health 	= 0
	# defines this movement speed
	__speed		= 0
	# this current score
	__score 	= 0
	# this current level
	__level		= 0

	def __init__(self):
		dimen = resource.get_dimen("player")
		GameObject.__init__(self, dimen)

		self.__health 	= resource.get_value("player_hp_start")
		self.__speed	= resource.get_value("player_mov_speed")

	def set_health(self, health):
		"""
		set current health
		:param health:
		:type health: int
		:return:
		"""
		self.__health = health

	def set_speed(self, speed):
		"""
		set this speed value
		:param speed: new speed value
		:type speed: int
		:return:
		"""
		self.__speed = speed

	def set_score(self, score):
		"""
		set this score
		:param score: new score value
		:type score: int
		:return:
		"""
		self.__score = score

	def set_level(self, level):
		"""
		set this level
		:param level:  new level value
		:type level: int
		:return:
		"""
		self.__level = level

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
		:return: current score attr
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

	def mod_health(self, diff):
		"""
		modify current health\n
		:param diff: modifying term: increase health: positive integer param, decrease health: negative integer param\n
		:type diff: int
		:return: health after modification
		"""
		h = self.get_health()
		self.set_health(h + diff)
		return self.get_health()

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
		:return: level value after modification
		"""
		level = self.get_level()
		self.set_level(level + diff)
		return self.get_level()

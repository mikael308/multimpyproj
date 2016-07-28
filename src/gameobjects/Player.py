import pygame
from GameObject import GameObject
import resource


class Player(GameObject):
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
	__speed		= 10

	def __init__(self, name, health):
		src = resource.get_imagesrc("player")
		
		player_img 	= pygame.image.load(src)
		GameObject.__init__(self, player_img)

		self.__name 	= name
		self.__health 	= health


	def set_health(self, health):
		"""
		set current health
		"""
		self.__health = health

	def set_speed(self, speed):
		"""
		get this speed value
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


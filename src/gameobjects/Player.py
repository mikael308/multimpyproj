import pygame
from GameObject import GameObject
import resource

"""
	defines the player

	author Mikael Holmbom
	ver 1.0
"""
class Player(GameObject):

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

	# set current health
	def set_health(self, health):
		self.__health = health

	# get this speed value
	def set_speed(self, speed):
		self.__speed = speed

	# get this name
	def get_name(self):
		return self.__name

	# get current health
	def get_health(self):
		return self.__health

	def get_speed(self):
		return self.__speed

	"""
	determines if this instance is alive
	"""
	def is_alive(self):
		return self.__health > 0


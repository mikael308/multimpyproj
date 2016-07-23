"""
	defines the player 

	author Mikael Holmbom
	ver 1.0
"""
import pygame
from GameObject import GameObject
import resource


class Player(GameObject):

	# name of this player
	__name 		= ""
	# this current health value
	__health 	= 0
	# defines this movement speed
	__speed		= 10

	def __init__(self, name, health):
		#s = resource.getString("klaatu")
		#print "klas : " + s
		src = resource.getImageSrc("player")
		
		playerImage 	= pygame.image.load(src)
		GameObject.__init__(self, playerImage)

		self.__name 	= name
		self.__health 	= health

	# set current health
	def setHealth(self, health):
		self.__health = health

	# get this speed value
	def setSpeed(self, speed):
		self.__speed = speed
	# fet this name
	def getName(self):
		return self.__name

	# get current health
	def getHealth(self):
		return self.__health

	def getSpeed(self):
		return self.__speed

	# determines if this instance is alive
	def isAlive(self):
		return self.__health > 0


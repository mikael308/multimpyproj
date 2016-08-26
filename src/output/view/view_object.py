import pygame
from pygame.sprite import Sprite


class ViewObject(Sprite):
	"""
	graphic object used in gameplay\n

	author Mikael Holmbom
	ver 1.0
	"""

	# this image
	__image		= None
	# this pygame.Rect
	__rect		= None
	# GameObject this view is representing
	__game_object = None

	def __init__(self, img, gameobject=None):
		"""

		:param img: view representing this ViewObject
		 :type img: pygame.Surface
		:param gameobject: instance this ViewObject will represent
		:type gameobject: src.game.GameObject
		"""
		pygame.font.init()

		Sprite.__init__(self)

		self.__image 	= img
		self.set_rect(img.get_rect())

		if gameobject is not None:
			self.set_gameobject(gameobject)

	def set_gameobject(self, gameobject):
		"""
		set a GameObject instance to this view
		:param gameobject:
		:return:
		"""
		self.__game_object = gameobject

	def set_rect(self, rect):
		"""
		set this rect\n
		:param rect: new rect\n
		:type rect: pygame.Rect
		:return: self
		"""
		self.__rect = rect
		return self

	def _set_image(self, img):
		"""
		set this image\n
		:param img: new image
		:return: self
		"""
		self.__image = img
		return self

	def move_pos(self, x, y):
		"""
		move current position\n
		:param x: X-axis direction\n
		:type x: int
		:param y: Y-axis direction\n
		:type y: int
		:return: None
		"""
		mod_rect 	= self.get_rect().move((x, y))
		self.set_rect(mod_rect)

	def set_pos(self, x, y):
		"""
		set object to absolute position
		:param x: x-axis position
		:type x: int
		:param y: y-axis position
		:type y: int
		:return: None
		"""
		if self.has_gameobject():
			self.get_gameobject().set_pos(x, y)

		self.get_rect().x = x
		self.get_rect().y = y

	def get_gameobject(self):
		"""
		get the gameobject this view is representing\n
		:return:
		"""
		return self.__game_object

	def get_dimen(self):
		"""
		get this dimension\n
		:return:
		"""
		if self.has_gameobject():
			return self.__game_object.get_dimen()
		else:
			return None

	def get_image(self):
		"""
		get this image\n
		:return:
		"""
		return self.__image

	def get_rect(self):
		"""
		get current rect\n
		:return:
		"""
		return self.__rect

	def get_logic_rect(self):
		"""
		get the logic Rect, the
		:return:
		"""
		if self.has_gameobject():
			return self.get_gameobject().get_rect()
		else:
			return None

	def get_pos(self):
		"""
		get this current center position\n
		:return: current position\n
		:returns: [x-position, y-position]
		"""
		return self.get_rect().x, self.get_rect().y

	def get_logic_pos(self):
		"""
		get the logic position of this view
		:return:
		"""
		if self.has_gameobject():
			return self.get_gameobject().get_pos()
		else:
			return None

	def get_width(self):
		"""
		get this visual width\n
		:return:
		"""
		return self.__image.get_width()

	def get_height(self):
		"""
		get this visual height\n
		:return:
		"""
		return self.__image.get_height()

	def render(self):
		"""
		render this object\n
		:return:
		"""
		return self.get_image()

	def has_gameobject(self):
		"""
		determine if this instance is representing a GameObject instance\n
		:return:
		"""
		return self.__game_object is not None


from pygame.sprite import Sprite


class GameObject(Sprite):
	"""
	graphic object used in gameplay

	author Mikael Holmbom
	ver 1.0
	"""

	# this image
	__image		= None
	# this pygame.Rect
	__rect		= None

	def __init__(self, img):
		# add args sprite and rect
		Sprite.__init__(self)

		self.__image 	= img
		self.set_rect(img.get_rect())

	def set_rect(self, rect):
		"""
		set this rect\n
		:param rect: new rect\n
		:type rect: pygame.Rect
		:return: None
		"""
		self.__rect = rect

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
		:param y: y-axis position
		:return:
		"""
		self.__rect.x = x
		self.__rect.y = y

	def get_image(self):
		"""
		get this image
		:return:
		"""
		return self.__image

	def get_rect(self):
		"""
		get current rect
		"""
		return self.__rect

	def get_pos(self):
		"""
		get this current center position\n
		:return: current position\n
		:returns: [x-position, y-position]
		"""
		return self.get_rect().center

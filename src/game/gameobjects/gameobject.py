from pygame.sprite import Sprite


class GameObject(Sprite):
	"""
	graphic object used in gameplay

	author Mikael Holmbom
	ver 1.0
	"""

	__dimen  	= None
	# this image
	__image		= None
	# this pygame.Rect
	__rect		= None

	def __init__(self, img, dimen):
		# add args sprite and rect
		Sprite.__init__(self)

		self.__dimen 	= dimen
		self.__image 	= img
		self.set_rect(img.get_rect())

		if dimen.x is not None and dimen.y is not None:
			self.set_pos(dimen.x, dimen.y)

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
		self.get_rect().x = x
		self.get_rect().y = y

		self.__dimen.x = x
		self.__dimen.y = y

	def get_image(self):
		"""
		get this image
		:return:
		"""
		return self.__image

	def get_dimen(self):
		"""
		get this dimension\n
		:return: this instance dimension
		"""
		return self.__dimen

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
		return self.get_rect().x, self.get_rect().y

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

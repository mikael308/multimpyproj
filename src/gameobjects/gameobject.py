import id


class GameObject:
	"""
	graphic object used in gameplay

	author Mikael Holmbom
	ver 1.0
	"""

	# this unique id
	__id 		= ""
	# this current sprite
	__sprite	= None
	# this current rectangle
	__rect		= None

	def __init__(self, sprite):
		# add args sprite and rect
		self.__id = id.get_id()
		self.__sprite 	= sprite
		self.__rect 	= sprite.get_rect()

	def set_sprite(self, sprite):
		"""
		set current sprite
		"""
		self.__sprite = sprite

	def set_rect(self, rect):
		"""
		set current rectangle
		"""
		self.__rect = rect

	def set_pos(self, x, y):
		"""
		set current position\n
		:param x: new X-axis position
		:param y: new Y-axis position
		:return:
		"""
		mod_rect 	= self.get_rect().move((x, y))
		self.set_rect(mod_rect)

	def get_sprite(self):
		"""
		get current sprite\n
		:return:
		"""
		return self.__sprite

	def get_rect(self):
		"""
		get current rect
		"""
		return self.__rect

	def get_pos(self):
		"""
		get this current center position
		:return: current position
		"""
		return self.get_rect().center

	def get_id(self):
		"""
		get this id
		:return:
		"""
		return self.__id
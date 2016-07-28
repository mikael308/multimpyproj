"""
graphic object used in gameplay

author Mikael Holmbom
ver 1.0
"""

class GameObject:

	# this current sprite
	__sprite	= None
	# this current rectangle
	__rect		= None

	__pos		= [0,0]


	def __init__(self, sprite):
		#add args sprite and rect
		self.__sprite 	= sprite
		self.__rect 	= sprite.get_rect()
		
	# set current sprite
	def set_sprite(self, sprite):
		self.__sprite = sprite
	# set current rect
	def set_rect(self, rect):
		self.__rect = rect
	def set_pos(self, x, y):
		self.__pos[0] = x
		self.__pos[1] = y

	# get current sprite
	def get_sprite(self):
		return self.__sprite

	"""
	get current rect
	"""
	def get_rect(self):
		return self.__rect

	def get_pos(self):
		return self.__pos
	"""
	get the centerposition of this rectangle
	"""
	def get_centerpos(self):
		x = self.get_pos()[0] - self.get_rect().width / 2
		y = self.get_pos()[1] - self.get_rect().height / 2

		return (x,y)

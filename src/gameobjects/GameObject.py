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
	def setSprite(self, sprite):
		self.__sprite = sprite
	# set current rect
	def setRect(self, rect):
		self.__rect = rect
	def setPos(self, x, y):
		self.__pos[0] = x
		self.__pos[1] = y

	# get current sprite
	def getSprite(self):	
		return self.__sprite

	"""
	get current rect
	"""
	def getRect(self):
		return self.__rect

	def getPos(self):
		return self.__pos
	"""
	get
	"""
	def getCenterPos(self):
		x = self.getPos()[0] - self.getRect().width / 2
		y = self.getPos()[1] - self.getRect().height / 2

		return (x,y)

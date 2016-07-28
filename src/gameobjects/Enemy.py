import resource, pygame
from GameObject import GameObject

class Enemy:

	__health = 0

	def __init__(self, health):
		src = resource.get_imagesrc("enemy")
		player_img = pygame.image.load(src)
		GameObject.__init__(self, player_img)

		self.__health = health


		
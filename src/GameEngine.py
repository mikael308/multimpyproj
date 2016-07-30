
import pygame, thread, time
import resource
from settings import controls


class GameEngine:
	"""
	gameengine for game
	gameloop: @see run(self)

	@author Mikael Holmbom
	"""

	__game_title 		= resource.get_string("game_title")
	__screen 			= None

	__bomb_flag 		= False
	__bomb 				= None

	# users gameobject
	__player 			= None
	__enemy				= None

	# contain current games CPUs
	__cpus				= {}
	# contain current games Packets
	__packets			= {}

	__end_state			= 0

	def __init__(self):
		"""
		initialize gameengine\n
		defines screen and init pygame
		"""
		
		size 			= (resource.get_dimen("main_window_size_width"),
						   resource.get_dimen("main_window_size_height"))
		self.__screen  	= pygame.display.set_mode(size)
		
		pygame.display.set_caption(self.__game_title)
		pygame.display.set_icon(GameEngine.loadImage("icon"))

		pygame.font.init()

	def __destruct(self):
		"""
		destructs this gameengine
		:return:
		"""
		pygame.font.quit()
		pygame.quit()

	def add_player(self, player):
		"""
		add client player to this gameengine
		"""

		self.__player = player

	@staticmethod
	def loadImage(imgId):
		return pygame.image.load(resource.get_imagesrc(imgId))

	def __handle_event(self, event):
		"""
		handles incoming event
		"""
		
		if event.type == pygame.QUIT:
			self.__destruct()

		if event.type == pygame.KEYDOWN:
			key = pygame.key.get_pressed()
			if key[controls.key_quit]:
				# quit gameloop
				self.__game_loop = False
				self.__end_state = 2	

			elif key[controls.key_action]:
				print "actionkey"
				pos = self.__player.get_centerpos()
				
				self.__plant_bomb(pos)
				
			else:
				##################
				## MOVEMENT
				##################
				movs = self.__input_movement(key, self.__player)
				x = movs[0]
				y = movs[1]
				
				#check if x and y is bigger than distance between gameobj and screensize
				self.__player = GameEngine.__move_gameobj(self.__player, movs)

		elif event.type == pygame.KEYUP:
			key = pygame.key.get_pressed()
			if key[controls.key_info]:
				print "info"
				pl = self.__player
				print pl.get_name() + " hp:" + str(pl.get_health())
				#print en.get_name() + " hp:" + str(en.getHealth())
				print " -"
				print ""

	@staticmethod
	def __move_gameobj(gameobj, movs):
		"""
		move gameobject with direction movs
		movs[0] - X -> positive:right, negative:left
		movs[1] - Y -> positive:down, negative:up
		"""
		rect = gameobj.get_rect()
		gameobj.set_rect(rect.move(movs[0], movs[1]))

		return gameobj

	def run(self):
		"""
		start this gameengine
		prior: player must be defined
		"""
		pygame.init()

		background 		= GameEngine.loadImage("background")
		enemyImage		= GameEngine.loadImage("enemy")
		health_icon 	= GameEngine.loadImage("health")

		
		#en 				= Enemy("tom", 10, enemyImage, 2, 3)

		self.__player = self.__move_object(self.__player, 100, 100)
		#en = self.__move_object(e

		# set key press repeat instantly as standard
		flag_key_repeat_inst = True
		pygame.key.set_repeat(21,21)

		self.__game_loop = True
	
		# GAME LOOP
		while self.__game_loop:
			for event in pygame.event.get():
				self.__handle_event(event)
			
			# display
			screen.blit(self.__player.get_sprite(), self.__player.get_rect())
			self.__screen.blit(background, (0, 0))

			if self.__bomb_flag:
				b = self.__bomb
				self.__screen.blit(b.get_sprite(), b.get_rect())

			pygame.display.update()

		# ! GAME LOOP
		# ending gameplay

		self.__update_endstate()
		self.__validate_endstate()

		self.__destruct()

	def __display_all_current(self):
		for x in self.__cpus.values():
			self.__display(x)

		for p in self.__packets.values():
			self.__display(p)

		self.__display(self.__player)


	def __display(self, gameobject):
		"""
		displays gameobject on current screen
		:param gameobject: gameobject to display
		:return:
		"""
		self.__screen.blit(gameobject.get_sprite(), gameobject.get_rect())

	def __validate_endstate(self):
		"""
		start endsequence according to this current endstate
		"""

		es = self.__end_state
		if es 		== -1:
			print "ERROR"
		elif es 	== 0:
			print "you died, you lost"
		elif es 	== 1:
			print "you defeated the enemy , you won the game!"
		elif es 	== 2:
			print "you quit the game"

	def __update_endstate(self):
		if not self.__player.is_alive():
			self.__end_state = 0
		
		"""if not en.is_alive():
			end_state = 1
			break
		"""


	"""
		make follower follow target with the speed of n
	"""
	"""
	def __ai_follow(self, follower, target, n):
		f 		= follower.get_rect()
		fs 		= follower.get_speed()
		
		tX		= target.get_rect().center[0]
		tY 		= target.get_rect().center[1]

		movX = 0
		movY = 0

		for i in range(n):
			if 		tX < f.left:		movX 	= fs *-1
			elif 	f.right < tX:		movX 	= fs 
			if 		f.top > tY:			movY 	= fs *-1
			elif 	tY > f.bottom:		movY 	= fs 

			f = f.move((movX, movY))

		follower.set_rect(f)
		return follower
	"""
	"""
	def __plant_bomb(self, pos):
		if not self.__bomb_flag:
			b 					= Obstacle_bomb(3)
			self.__bomb_flag 	= True
			self.__bomb 		= self.__move_object(b, pos[0], pos[1])

			#TODO params are wierd....
			thread.start_new_thread(self.__explode, ("klaatu", 3))
	"""		

	"""

	move to bomb bostale class?
	and chekc for collission right before call??

	"""
	"""
	def __explode(self, msg, delay):

		time.sleep(delay)
		
		b = self.__bomb
		#b.set_sprite(b.get_sprite_explosion())

		s_b_expl = b.get_sprite_explosion()
		#bsprite = b.get_sprite()
		scalesize = 50
		for i in range(0,3):
			time.sleep(0.02)
			b.set_sprite(pygame.transform.smoothscale(s_b_expl, (scalesize *i, scalesize *i)))
			rect = b.get_rect();
			b.set_rect(rect.move((scalesize / 5) *-1 , (scalesize/5) *-1)) # move bomb explosion as it expands


		b.get_rect().inflate(30, 30)
		print "  > BOOOM!!"
		# ENEMY HIT?
		if self.__enemy.get_rect().colliderect(self.__bomb.get_rect()):
			print " > HIT!"
			self.__enemy.do_damage(b.get_damage())
		else:
			print " - MISS"

		# PLAYER HIT?
		if self.__player.get_rect().colliderect(self.__bomb.get_rect()):
			print " you where hit!"
			self.__player.do_damage(b.get_damage())
		else:
			print "the bomb missed you"

		time.sleep(2)
		self.__bomb_flag = False

	"""

	def __move_object(self, obj, x, y):
		"""
		move obj to absolute position (x, y)
		"""
		w 		= obj.get_rect().width
		h 		= obj.get_rect().height

		# edit the rectangle
		rect 	= pygame.Rect((0,0), (w, h))
		rect 	= rect.move((x, y))

		obj.set_rect(rect)
		return obj

	def __input_movement(self, key, gameobject):
		"""
		moves gameobject according to input movement
		return movement direction as list [X, Y]
		"""

		rect 		= gameobject.get_rect()
		mov_speed 	= gameobject.get_speed()
		ddir 		= 0.7 # diagonal direction: factor multiplied to distance on diagonal movement

		left 	= controls.key_mov_left
		right 	= controls.key_mov_right
		up 		= controls.key_mov_up
		down 	= controls.key_mov_down

		def __get_mov_x(key):
			"""
			inner function
			get X-axis movement from key
			if no movement was found, 0 is returned
			"""
			if key[left]:
				dist = rect.left # distance to wall
				if dist < mov_speed:
					return dist * -1
				else:
					return mov_speed * -1

			elif key[right]:
				dist = self.__screen.get_width() - rect.right # distance to wall
				if dist < mov_speed:
					return dist
				else:
					return mov_speed
			else:
				return 0

		def __get_mov_y(key):
			"""
			inner function
			get Y-axis movement from key
			if no movement was found, 0 is returned
			"""
			if key[up]:
				dist = rect.top # distance to wall
				if dist < mov_speed:
					return dist * -1
				else:
					return mov_speed * -1
			elif key[down]:
				dist = self.__screen.get_height() - rect.bottom # distance to wall
				if dist < mov_speed:
					return dist
				else:
					return mov_speed
			else:
				return 0

		mov_x = __get_mov_x(key)
		mov_y = __get_mov_y(key)

		# (up left) |  (up right)
		if mov_x != 0 and mov_y != 0:
			if mov_x > 1:
				mov_x *= ddir
			if mov_y > 1:
				mov_y *= ddir

		return (mov_x, mov_y)

	def __slow_key(self):
		"""
		gets current key event slow delay and interval
		sets keys to instant repeat again after used
		"""
		pygame.key.set_repeat(60000,60000)
		pygame.key.set_repeat(21,21)


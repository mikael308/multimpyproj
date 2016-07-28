"""
	@author Mikael Holmbom

	gameengine for game
	gameloop: @see run(self)

"""
import pygame, thread, time
import resource
from gameobjects import Player
from settings import controls


class GameEngine:

	__game_title 		= resource.getString("game_title")

	__screen 			= None
	__screen_width		= resource.getDimen("main_window_size_width")
	__screen_height		= resource.getDimen("main_window_size_height")

	__bomb_flag 		= False
	__bomb 				= None

	# users gameobject
	__player 			= None
	__enemy				= None

	__end_state			= 0


	def __init__(self):
		
		size 			= (self.__screen_width, self.__screen_height)
		self.__screen  	= pygame.display.set_mode(size)
		
		pygame.display.set_caption(self.__game_title)
		pygame.display.set_icon(GameEngine.loadImage("icon"))

		pygame.font.init()

	def __destruct(self):
		pygame.quit()
		
	"""
		add client player to this gameengine
	"""
	def add_player(self, player):
		self.__player = player

	@staticmethod
	def loadImage(imgId):
		return pygame.image.load(resource.getImageSrc(imgId))

	"""
		handles incoming event
	"""
	def __handle_event(self, event):
		
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
				pos = self.__player.getCenterPos()
				
				self.__plant_bomb(pos)
				
			else:
				##################
				## MOVEMENT
				##################
				movs = self.__input_movement(key, self.__player)
				x = movs[0]
				y = movs[1]
				
				#check if x and y is bigger than distance between gameobj and screensize
				self.__player = GameEngine.__moveGameObj(self.__player, movs)

		elif event.type == pygame.KEYUP:
			key = pygame.key.get_pressed()
			if key[controls.key_info]:
				print "info"
				pl = self.__player
				print pl.getName() + " hp:" + str(pl.getHealth())
				#print en.get_name() + " hp:" + str(en.getHealth())
				print " -"
				print ""

	@staticmethod
	def __moveGameObj(gameobj, movs):
		rect = gameobj.getRect()
		gameobj.setRect(rect.move(movs[0], movs[1]))

		return gameobj

	"""
	start this gameengine
	prior: player must be defined
	"""
	def run(self):
		pygame.init()

		screen 			= self.__screen

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
			screen.blit(background, (0,0))
			screen.blit(self.__player.getSprite(), self.__player.getRect())

			if self.__bomb_flag:
				b = self.__bomb
				screen.blit(b.getSprite(), b.getRect())

			pygame.display.update()

		# ! GAME LOOP
		# ending gameplay

		self.__update_endstate()
		self.__validate_endstate()

		self.__destruct()


	"""
		start endsequence according to this current endstate
	"""
	def __validate_endstate(self):

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
		if not self.__player.isAlive():
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
	
	
	# move obj to absolute position (x, y)
	def __move_object(self, obj, x, y):
		w 		= obj.getRect().width
		h 		= obj.getRect().height

		# edit the rectangle
		rect 	= pygame.Rect((0,0), (w, h))
		rect 	= rect.move((x, y))

		obj.setRect(rect)
		return obj
	
	"""
		moves gameobject according to input movement
		return movement direction as list [X, Y]
	"""
	def __input_movement(self, key, gameobject):
		movX 		= 0
		movY 		= 0

		rect 		= gameobject.getRect()
		mov_speed 	= gameobject.getSpeed()
	 	ddir 		= 0.7

		l 	= controls.key_mov_left
		r 	= controls.key_mov_right
		u 	= controls.key_mov_up
		d 	= controls.key_mov_down

		print "rect"
		print "bottom:" + str(rect.bottom) + "    top:" + str(rect.top)
		print "left:" + str(rect.left) + "     right:"+str(rect.right) 
		
		# inner function
		# get X-axis movement from key
		# if no movement was found, 0 is returned
		def __getMovX(key):
			if key[l] and rect.left > 0:
				## if movement is higher than distance to wall
				#if rect.left < mov_speed:
				#	return rect.left

				return mov_speed * -1

			elif key[r] and rect.right < self.__screen_width:
				## if movement is higher than distance to wall
				#if rect.right < mov_speed:
				#	return rect.right

				return mov_speed
			else:
				return 0

		# 	(up) 
		if key[u] and rect.top > 0: 
			movY = mov_speed * -1
			movX = __getMovX(key)

			# (up left) |  (up right)
			if movX != 0:
				movX *= ddir
				movY *= ddir

		# 	(down)
		elif key[d] and rect.bottom < self.__screen_height:
			movY = mov_speed 
			movX = __getMovX(key)
			
			# (down left) |  (down right)
			if movX != 0:
				movX *= ddir
				movY *= ddir

		# 	(left) | (right)
		else:
			movX = __getMovX(key)

		return (movX, movY)

	"""
		gets current key event slow delay and interval
		sets keys to instant repeat again after used
	"""
	def __slow_key(self):
		pygame.key.set_repeat(60000,60000)
		pygame.key.set_repeat(21,21)


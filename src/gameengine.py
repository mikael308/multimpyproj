import pygame, resource
from random import randint
from settings import controls
from gameobjects.attachable import Attachable
from gameobjects.cpu import CPU
from gameobjects.packet import Packet
from screen import Screen
from buffer import Buffer


class GameEngine:
	"""
	gameengine for game
	gameloop: @see run(self)

	@author Mikael Holmbom
	"""

	__game_title 		= resource.get_string("game_title")
	__screen 			= None

	## GAMELOGIC
	####################
	# time
	__clock				= None
	__FPS				= resource.get_value("fps")
	__holdtime			= 1000 / __FPS
	__timespan_add_packet = resource.get_value("timespan_add_packet_start")
	__timespan_add_packet_factor_decr_factor = resource.get_value("timespan_add_packet_factor_decr_factor")



	## GAMEOBJECTS
	###################
	# users gameobject
	__player 			= None
	__points_to_next_level = resource.get_value("points_exp_level_up_start")
	__points_exp_needed_factor = resource.get_value("points_exp_needed_factor")

	# contain current games CPUs
	__cpus				= []
	# contain current games Packets

	__end_state			= 0
	__packets			= []
	__buf_capacity 		= resource.get_value("buf_capacity")
	__buf				= Buffer(__buf_capacity)

	def __init__(self):
		"""
		initialize gameengine\n
		defines screen and init pygame
		"""

		pygame.display.set_caption(self.__game_title)
		pygame.display.set_icon(GameEngine.load_image("icon"))

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
		add client player to this gameengine\n
		:param player: the player of this game\n
		:return:
		"""

		self.__player = player

	@staticmethod
	def load_image(img_id):
		return pygame.image.load(resource.get_imagesrc(img_id))

	def __handle_event(self, event):
		"""
		handles incoming event
		:param event: the event to handle
		:return:
		"""
		
		if event.type == pygame.QUIT:
			self.__destruct()

		if event.type == pygame.KEYDOWN:
			key = pygame.key.get_pressed()
			if key[controls.key_quit]:
				# quit gameloop
				self.__game_loop = False
				self.__end_state = 2	


			###############################################
			# DEBUG
			if key[pygame.K_a]:
				print "add packet!"
				self.__add_packet()
			if key[pygame.K_b]:
				print "buf:" + str(self.__buf)
			if key[pygame.K_k]:
				print "kill player by 1"
				self.__player.damage(1)

				print "player health: " + str(self.__player.get_health())

			if key[pygame.K_s]:
				print "SCORE!!!"
				self.__player.mod_score(1)

			if key[pygame.K_p]:
				print "my packets"
				for p in self.__packets:
					print " * " + str(p.get_val())
			# ! DEBUG
			####################################################
			elif key[controls.key_action]:

				if self.__player.has_attached():
					attobj = self.__player.get_attached()
					self.__player.detach()
					for cpu in self.__cpus:
						if attobj.get_rect().colliderect(cpu.get_rect()):
							del self.__packets[attobj.get_id()]
							if attobj.get_val() == cpu.get_val():
								self.__player.mod_score(1)
							else:
								self.__player.mod_score(-1)

				else:
					for p in self.__packets.values():
						pp = p.get_rect().center[1]
						plp = self.__player.get_rect().center[1]
						if pp - 20 < plp and plp < pp + 20:
							self.__player.attach(p)

			else:
				##################
				## MOVEMENT
				##################
				movs = self.__input_movement(key, self.__player)

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
		:param gameobj:
		:param movs: movs[0] - X -> positive:right, negative:left\n
		movs[1] - Y -> positive:down, negative:up
		:return: edited gameobj with new position
		"""
		rect = gameobj.get_rect()
		gameobj.set_rect(rect.move(movs[0], movs[1]))

		if isinstance(gameobj, Attachable) and gameobj.has_attached():
			GameEngine.__move_gameobj(gameobj.get_attached(), movs)

		return gameobj

	def run(self):
		"""
		start this gameengines gameloop\n
		prior -- player must be defined, see add_player(self)
		:return:
		"""
		pygame.init()

		size = (resource.get_dimen("main_window_size_width"),
				resource.get_dimen("main_window_size_height"))

		self.__screen = Screen(size, self.__player, self.__buf, self.__cpus, self.__packets)
		self.__setup_gameobjects()

		# set key press repeat instantly as standard
		flag_key_repeat_inst = True
		pygame.key.set_repeat(21,21)

		self.__game_loop = True
		self.__clock = pygame.time.Clock()
		self.__time = 0
		# GAME LOOP ####################################
		while self.__game_loop:
			for event in pygame.event.get():
				self.__handle_event(event)


			clock.tick(self.__FPS)

		# ending gameplay
			if not self.__player.is_alive():
				self.__game_loop = False
			self.__screen.render()

		# ! GAME LOOP ###################################

		self.__update_endstate()
		self.__validate_endstate()

		self.__destruct()

	def __gamelogic(self):
		# delay framerate
		self.__time += self.__clock.tick(self.__FPS)

		# if player reaches x scores:
		# 	* player level up
		# 	* increase the next amount of scores to level up again
		# 	* decrease timespan between every new added packet
		if self.__player.get_score() >= self.__points_to_next_level:
			self.__points_to_next_level *= self.__points_exp_needed_factor
			self.__timespan_add_packet *= self.__timespan_add_packet_factor_decr_factor

			print " ********** lvl up"
			print "\tpoints need next lvl : " + str(self.__points_to_next_level)
			print "\ttimespan add packet  : " + str(self.__timespan_add_packet)


		# spawn new packets every x second
		if self.__time % self.__timespan_add_packet < self.__holdtime:
			print "add packet according to time"
			self.__add_packet()

			print " ==== " + str(self.__time / 1000) + "s"
			print "      rest : " + str()

		if not self.__player.is_alive():
			self.__game_loop = False

	def __setup_gameobjects(self):
		"""
		setup gameobjects
		:return:
		"""
		packet_val_max = resource.get_value("packet_val_max")
		packet_val_min = resource.get_value("packet_val_min")

		num = resource.get_value("n_cpus")

		vals = []
		while len(vals) < num:
			v = randint(packet_val_min, packet_val_max)
			if vals.count(v) == 0:
				vals.append(v)
				cpu = CPU(v)
				cpu.set_pos(400, 75 * len(vals) + 10)
				self.__cpus.append(cpu)

		src = resource.get_imagesrc("health")
		self.__health_icon = pygame.image.load(src)

		for i in range(0, resource.get_value("buf_size_start")):
			self.__add_packet()

		self.__player.set_pos(resource.get_value("player_startpoint_x"), resource.get_value("player_startpoint_y"))

	def __validate_endstate(self):
		"""
		start endsequence according to this current endstate
		:return:
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


	def __input_movement(self, key, gameobject):
		"""
		moves gameobject according to input movement
		return movement direction as list [X, Y]
		:param key: the pressed key
		:param gameobject: the gameobject to move
		:return: movement as tuple (x_movement, y_movement)
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
			:param key: pressed key
			:return: movement of X-axis
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
			:param key: pressed key
			:return: movement of Y-axis
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

		# get left and right movements
		mov_x = __get_mov_x(key)
		mov_y = __get_mov_y(key)

		if mov_x != 0 and mov_y != 0:
			# if diagonally movement
			if mov_x > 1:
				mov_x *= ddir
			if mov_y > 1:
				mov_y *= ddir

		return mov_x, mov_y

	def __slow_key(self):
		"""
		gets current key event slow delay and interval
		sets keys to instant repeat again after used
		:return:
		"""
		pygame.key.set_repeat(60000,60000)
		pygame.key.set_repeat(21,21)

	def __add_packet(self):
		n_cpu = len(self.__cpus)
		val_idx = randint(0, n_cpu - 1)
		val = self.__cpus[val_idx].get_val()

		p = Packet(val)
		y = 400 - (50 * len(self.__packets))
		p.set_pos(20, y)

		self.__packets[p.get_id()] = p


	def __grab_packet(self, packet):
		"""
		player grabs a packet
		:param packet:
		:return:
		"""
		self.__buf.delete(packet)
		self.__player.attach(packet)

	def __release_packet(self):
		"""
		player releases the attached packet
		:return:
		"""
		attobj = self.__player.get_attached()
		self.__player.detach()
		for cpu in self.__cpus:
			if attobj.get_rect().colliderect(cpu.get_rect()):
				self.__packets.remove(attobj)
				if attobj.get_val() == cpu.get_val():
					self.__player.mod_score(1)
				else:
					self.__player.mod_score(-1)


import pygame, resource, tools, traceback
from random import randint
from settings import controls, settings
from gameobjects.attachable import Attachable
from gameobjects.cpu import CPU
from gameobjects.packet import Packet
from output import Output
import game_objects


class GameEngine:
	"""
	gameengine for game\n
	To run this, see run(self)\n
	gameloop: @see start(self)

	:author: Mikael Holmbom
	:version: 1.0
	"""

	__game_title 		= resource.get_string("game_title")
	__output 			= None

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
	__player 			= game_objects.get_player()
	__points_to_next_level = resource.get_value("points_exp_level_up_start")
	__points_exp_needed_factor = resource.get_value("points_exp_needed_factor")

	# contain current games CPUs
	__cpus				= game_objects.get_cpus()
	# contain current games Packets

	__end_state			= 0
	__packets			= game_objects.get_packets()
	__buf				= game_objects.get_buf()

	def __init__(self):
		"""
		initialize gameengine\n
		defines screen and init pygame
		"""
		pygame.display.set_caption(self.__game_title)
		pygame.display.set_icon(GameEngine.load_image("icon"))

	def __destruct(self):
		"""
		destructs this gameengine
		:return:
		"""
		pygame.quit()

	def run(self):
		"""
		start this gameengines gameloop\n
		prior -- player must be defined, see add_player(self)
		:return:
		"""
		try:
			self.__start()

		except Exception as e:
			traceback.print_exc()
			self.__destruct()

	def __start(self):
		"""
		the startpoint of this gameengine
		:return:
		"""
		pygame.init()

		self.__setup_gameobjects()
		self.__output = Output()

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

			self.__gamelogic()

			self.__output.render()

		# ! GAME LOOP ###################################

		self.__update_endstate()
		self.__validate_endstate()


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
				self.__score()

			if key[pygame.K_p]:
				print "my packets"
				for p in self.__packets:
					print " * " + str(p.get_val())
			# ! DEBUG
			####################################################
			elif key[pygame.K_m]:
				settings.switch_soundfx_enabled()

			elif key[controls.key_action]:

				if self.__player.has_attached():
					self.__release_packet()

				else:
					for p in self.__packets:
						pr = p.get_rect()
						plr = self.__player.get_rect()
						if pr.colliderect(plr):
							self.__grab_packet(p)

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
		try:
			self.__start()

		except Exception as e:
			traceback.print_exc()
		finally:
			self.__destruct()

	def __start(self):
		"""
		the startpoint of this gameengine
		:return:
		"""
		pygame.init()

		size = (resource.get_dimen("main_window_size_width"),
				resource.get_dimen("main_window_size_height"))

		self.__setup_gameobjects()
		self.__screen = Screen(size)
		self.__screen\
			.set_player(self.__player)\
			.set_buffer(self.__buf)\
			.set_cpus(self.__cpus) \
			.set_packets(self.__packets)
		self.__screen.setup()

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

			self.__gamelogic()

			self.__screen.render()

		# ! GAME LOOP ###################################

		self.__update_endstate()
		self.__validate_endstate()

		self.__destruct()

	def __gamelogic(self):
		"""
		gamelogic defined
		:return:
		"""
		# delay framerate
		self.__time += self.__clock.tick(self.__FPS)

		# if player reaches x scores:
		# 	* player level up
		# 	* increase the next amount of scores to level up again
		# 	* decrease timespan between every new added packet
		if self.__player.get_score() >= self.__points_to_next_level:
			self.__level_up()

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

		n_cpus = resource.get_value("n_cpus")

		# generates cpus with unique values
		vals = tools.unique_vals(n_cpus, packet_val_min, packet_val_max)
		for val in vals:
			cpu = CPU(val)
			self.__cpus.append(cpu)

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
		ddir 		= 0.7  # diagonal direction: factor multiplied to distance on diagonal movement

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
				dist = self.__output.get_screen().get_width() - rect.right  # distance to wall
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
				dist = rect.top  # distance to wall
				if dist < mov_speed:
					return dist * -1
				else:
					return mov_speed * -1
			elif key[down]:
				dist = self.__output.get_screen().get_height() - rect.bottom  # distance to wall
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

	def __generate_packet(self):
		"""
		generates a packet with value from current cpus
		:return:
		"""
		n_cpu = len(self.__cpus)
		val_idx = randint(0, n_cpu - 1)
		val = self.__cpus[val_idx].get_val()
		p = Packet(val)

		return p

	def __add_packet(self):
		"""
		generates a new packet and adds it to game:\n
		if buffer is full -> buffer overflow\n
		else add packet to buffer
		:return:
		"""
		p = self.__generate_packet()

		if self.__buf.add(p):
			if self.__output:
				self.__output.update()
			self.__packets.append(p)

		else:
			self.__buffer_overflow()

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
					self.__score()
				else:
					self.__wrong_cpu()

	def __buffer_overflow(self):
		"""
		simulates the effect of a buffer overflow
		:return:
		"""
		self.__player.damage(1)

	def __packet_timeout(self, packet):
		"""
		simulates the effect of timeout of packet
		:param packet:
		:return:
		"""
		self.__player.mod_score(-1)

	def __score(self):
		"""

		:return:
		"""
		self.__output.score()

		self.__player.mod_score(1)

	def __wrong_cpu(self):
		self.__output.wrong_cpu()

		self.__player.mod_score(-1)

	def __level_up(self):
		self.__output.level_up()

		self.__points_to_next_level *= self.__points_exp_needed_factor
		self.__timespan_add_packet *= self.__timespan_add_packet_factor_decr_factor
		self.__player.mod_level(1)

		print " ********** lvl up"
		print "\tpoints need next lvl : " + str(self.__points_to_next_level)
		print "\ttimespan add packet  : " + str(self.__timespan_add_packet)
		print "\tplayer level         : " + str(self.__player.get_level())


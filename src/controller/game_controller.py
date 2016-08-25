import pygame
from random import randint
from src.game.gameobjects.trash import Trash
import src.resource.resource as resource
import src.tools as tools
from src.buffer import Buffer
from src.controller.controller import Controller
from src.game.gameobjects.packet import Packet
from src.game.gameobjects.player import Player
from src.game.gameobjects.cpu import CPU


class GameController(Controller):
	"""
	controller for game use-case\n

	:author: Mikael Holmbom
	:version: 1.0
	"""
	__game_title = resource.get_string("game_title")

	__gamefield_dimen = resource.get_dimen("gamefield")

	## GAMELOGIC
	####################
	__timespan_add_packet = resource.get_value("timespan_add_packet_start")
	__timespan_add_packet_factor_decr_factor = resource.get_value("timespan_add_packet_factor_decr_factor")

	## GAMEOBJECTS
	###################
	# users gameobject
	__player 			= None
	__points_to_next_level = resource.get_value("points_exp_level_up_start")
	__points_exp_needed_factor = resource.get_value("points_exp_needed_factor")

	# contain current games CPUs
	__cpus				= None
	# current packets not contained in buffer
	__pending_packet	= None
	__buffer			= None
	__trash				= None
	"""
	memento object of this instance
	"""
	__memento			= None

	def __init__(self):
		"""
		initialize gameengine\n
		defines screen and init pygame
		"""
		Controller.__init__(self)

		self.__player 	= Player()
		self.__buffer 		= Buffer(resource.get_value("buffer_capacity"))
		self.__cpus 	= []
		self.__pending_packet 	= []

	def setup(self):
		"""
		setup the attributes of this gameengine\n
		:return:
		"""

		Controller.setup(self)

		self.__create_memento()

		n_cpus = resource.get_value("n_cpus")
		packet_val_min = resource.get_value("packet_val_min")
		packet_val_max = resource.get_value("packet_val_max")

		self.__trash = Trash()
		trash_dimen = resource.get_dimen("trash")
		self.__trash.set_pos(trash_dimen.x, trash_dimen.y)

		# generates cpus with unique values
		vals = tools.unique_vals(n_cpus, packet_val_min, packet_val_max)
		for val in vals:
			self.__cpus.append(CPU(val))

		for i in range(0, resource.get_value("buffer_size_start")):
			self.add_packet()

		player_dimen = resource.get_dimen("player")
		self.__player.set_pos(player_dimen.x, player_dimen.y)

	@staticmethod
	def load_image(img_id):
		return pygame.image.load(resource.get_imagesrc(img_id))

	def __collide_detection(self, obj, (x, y)):
		"""
		detect if movement will result in a collision with wall, if so the movements will be modified to not collide\n
		:param obj: object to determine collision
		:type obj: src.game.gameobjects.GameObject
		:param (x, y): the relative movement direction
		:type (x, y): (int, int)
		:return: the
		"""
		o_rect = obj.get_rect()
		## COLLISION WITH WALL
		gf_w, gf_h = self.get_gamefield_dimen().wh()

		if x < 0:  # left movement
			dist = o_rect.left
			if dist + x < 0:
				x = dist * -1 # -1 because of negative direction
		elif x > 0:  # right movement
			dist = gf_w - o_rect.right
			if x > dist:
				x = dist

		if y < 0:  # up movement
			dist = o_rect.top
			if dist + y < 0:
				y = dist * -1 # -1 because of negative direction
		elif y > 0:  # down movement
			dist = gf_h - o_rect.bottom
			if y > dist:
				y = dist

		return x, y

	def get_gamefield_dimen(self):
		"""
		get the dimension of gamefield\n
		:return:
		"""
		return self.__gamefield_dimen

	def get_points_to_next_level(self):
		"""
		get the current treshold amount of points needed to get to next level\n
		:return:
		"""
		return self.__points_to_next_level

	def get_timespan_add_packet(self):
		"""
		get the amount of milliseconds timespan between every generated packet\n
		:return:
		"""
		return self.__timespan_add_packet

	def get_player(self):
		"""
		get the current player\n
		:return:
		"""
		return self.__player

	def get_cpus(self):
		"""
		get current list of cpus\n
		:return:
		"""
		return self.__cpus

	def get_packets(self):
		"""
		get a copy list of all current of packets from buffer and not in buffer\n
		:return:
		"""
		packets = list(self.get_pending_packets())
		for p in self.get_buffer():
			packets.append(p)

		return packets

	def get_pending_packets(self):
		return self.__pending_packet

	def get_buffer(self):
		"""
		get the buffer containing packets from this instance attr packets\n
		:see: get_packets(self) for all current packets\n
		:return:
		"""
		return self.__buffer

	def get_trash(self):
		"""
		get current trash instance
		:return:
		"""
		return self.__trash

	def __create_memento(self):
		"""
		create memento of this gameengine current state\n
		:see: __restore_memento(self)\n
		:return:
		"""
		class Memento:
			points_to_next_level 	= 0
			timespan_add_packet 	= 0
			player_score 			= 0
			player_level			= 0

		mem = Memento()
		mem.points_to_next_level 	= self.__points_to_next_level
		mem.timespan_add_packet		= self.__timespan_add_packet
		mem.player_score 			= self.__player.get_score()
		mem.player_level			= self.__player.get_level()
		self.__memento = mem

	def __restore_memento(self):
		"""
		restore gameengine from last created memento\n
		:see: __create_memento(self)\n
		:return:
		"""
		self.__points_to_next_level 	= self.__memento.points_to_next_level
		self.__timespan_add_packet		= self.__memento.timespan_add_packet
		if self.__player.get_score() > self.__memento.player_score:
			self.__player.set_score(self.__memento.player_score)
		if self.__player.get_level() > self.__memento.player_level:
			self.__player.set_score(self.__memento.player_level)

	def generate_packet(self):
		"""
		generates a packet with value from current cpus\n
		:return:
		"""
		n_cpu = len(self.__cpus)
		sender_idx, receiver_idx = tools.unique_vals(2, 0, n_cpu - 1)
		sender = self.get_cpus()[sender_idx].get_adress()
		receiver = self.get_cpus()[receiver_idx].get_adress()

		checksum = 0
		if randint(0, 4) == 0:
			# create incorrect checksum
			checksum = sender | receiver >> 1
		else:
			# create correct checksum
			checksum = sender & receiver

		p = Packet(sender, receiver, checksum)

		return p

	def add_packet(self):
		"""
		generates a new packet and adds it to game:\n
		if buffer is full -> buffer overflow\n
		else add packet to buffer\n
		:return: True if packet was added correct\nFalse if buffer overflow
		"""
		p = self.generate_packet()
		if self.get_buffer().add(p):
			return True

		else:
			self.buffer_overflow()
			return False

	def grab_packet(self, packet):
		"""
		player grabs a packet\n
		:param packet:
		:return:
		"""
		self.get_buffer().delete(packet)
		self.get_pending_packets().append(packet)
		self.get_player().attach(packet)

	def release_packet(self):
		"""
		player releases the attached packet\n
		:return: returns a flag as of:\n
		:returns -1: packet was placed at wrong position\n
		:returns 0: packet was placed on ground\n
		:returns 1: packet was placed at correct position ( cpu | trash )\n
		"""
		attobj = self.get_player().detach()
		for cpu in self.__cpus:
			if attobj.get_rect().colliderect(cpu.get_rect()):
				self.get_pending_packets().remove(attobj)
				if attobj.get_receiver() == cpu.get_adress()\
						and attobj.valid_checksum():
					self.score()
					return 1
				else:
					self.wrong_cpu()
					return -1

		if attobj.get_rect().colliderect(self.get_trash().get_rect()):
			self.get_pending_packets().remove(attobj)
			if attobj.valid_checksum():
				self.wrong_cpu()
				return -1
			else:
				self.score()
				return 1

		return 0

	def buffer_overflow(self):
		"""
		simulates the effect of a buffer overflow\n
		:return:
		"""
		self.__player.mod_health(-1)

	def packet_timeout(self, packet):
		"""
		simulates the effect of timeout of packet\n
		:param packet:
		:return:
		"""
		self.__player.mod_score(-1)

	def score(self):
		"""
		simulates the effect of getting +1 score\n
		:return:
		"""
		self.__player.mod_score(1)

	def wrong_cpu(self):
		"""
		simulates the effect releasing the wrong packet to wrong cpu\n
		:return:
		"""
		self.__restore_memento()

	def level_up(self):
		"""
		simulates the effect of player level up\n
		:return:
		"""
		self.__points_to_next_level *= self.__points_exp_needed_factor
		self.__timespan_add_packet 	*= self.__timespan_add_packet_factor_decr_factor
		self.__player.mod_level(1)

		self.__create_memento()

	def mov_player(self, (dir_x, dir_y)):
		"""
		move player position relative to current position\n
		:param dir_x: the X-axis direction to move player\n
		:type dir_x: int, ( -1 | 0 | 1 )
		:param dir_y: the Y-axis direction to move player\n
		:type dir_y: int, ( -1 | 0 | 1 )
		:return: players new modified position
		"""
		dir_x *= self.__player.get_speed()
		dir_y *= self.__player.get_speed()

		dir_x, dir_y = self.__collide_detection(self.__player, (dir_x, dir_y))
		self.__player.move_pos(dir_x, dir_y)
		r = self.get_player().get_rect()

		return self.get_player().get_pos()

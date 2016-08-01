
"""
	main start
	startup gameengine

	author: Mikael Holmbom
	ver 1.0
"""
import resource
from gameengine import GameEngine
from gameobjects.player import Player

player = Player("mikael", resource.get_value("player_hp_start"), resource.get_value("player_mov_speed"))

ge = GameEngine()
ge.add_player(player)
ge.run()




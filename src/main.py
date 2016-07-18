
"""
	main start
	startup gameengine

	author: Mikael Holmbom
	ver 1.0
"""
from GameEngine import GameEngine
from gameobjects import Player


player	= Player.Player("mikael", 3)

ge = GameEngine()
ge.add_player(player)
ge.run()




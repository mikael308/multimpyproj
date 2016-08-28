
"""
	main start\n
	runs StartMenuInterface\n

	:author: Mikael Holmbom
	:version: 1.0
"""
from interface.startmenu_interface import StartMenuInterface


def start_game():
    i = StartMenuInterface()
    i.setup()
    i.run()
    i.shutdown()


start_game()




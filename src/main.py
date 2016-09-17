
"""
	main start\n
	runs StartMenuInterface\n

	:author: Mikael Holmbom
	:version: 1.0
"""

import sys, os

path = os.getcwd() 
sys.path.append(path)

from src.interface.startmenu_interface import StartMenuInterface


def start_game():
    i = StartMenuInterface()
    i.maindisplay()


start_game()

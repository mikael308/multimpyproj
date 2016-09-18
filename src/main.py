
"""
	main start\n
	runs StartMenuInterface\n

	:author: Mikael Holmbom
	:version: 1.0
"""

import sys, os

path = os.getcwd() 
sys.path.append(path)

import pygame
import src.resource.resource as resource
from src.interface.startmenu_interface import StartMenuInterface


def start_game():
    i = StartMenuInterface()
    pygame.display.set_caption(resource.get_string("game_title"))
    i.maindisplay()


start_game()

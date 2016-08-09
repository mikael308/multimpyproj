import resource
from buffer import Buffer
from gameobjects.player import Player

"""
holding current gameobjects

"""


__player        = Player("player", resource.get_value("player_hp_start"), resource.get_value("player_mov_speed"))
__cpus          = []
__packets       = []
__buf			= Buffer(resource.get_value("buf_capacity"))

def get_player():
    return __player


def get_cpus():
    return __cpus


def get_packets():
    return __packets


def get_buf():
    return __buf


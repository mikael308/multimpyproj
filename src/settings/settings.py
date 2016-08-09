"""
settings access functions

:author: Mikael Holmbom
:version: 1.0
"""
import src.resource

__soundfx_enabled = True

__FPS = src.resource.get_value("fps")
__holdtime = 1000 / __FPS

def is_soundfx_enabled():
    return __soundfx_enabled


def switch_soundfx_enabled():
    """
    switch the value of setting: soundfx enabled
    :return:
    """
    __soundfx_enabled = not is_soundfx_enabled()
    print "soundfx is " + str(__soundfx_enabled)


def get_FPS():
    """
    get FPS value as of resource
    :return:
    """
    return __FPS


def get_holdtime():
    """
    get the holdtime, that is 1 000ms / FPS
    :return:
    """
    return __holdtime

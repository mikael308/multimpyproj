"""
settings access functions\n

:author: Mikael Holmbom
:version: 1.0
"""
import src.resource.resource as resource

__soundfx_enabled = False

__FPS = resource.get_value("fps")
__holdtime = 1000 / __FPS


def is_soundfx_enabled():
    """
    determine if sound effects is enabled\n
    :return:
    """
    return __soundfx_enabled


def switch_soundfx_enabled():
    """
    switch the value of setting: soundfx enabled\n
    :return:
    """
    global __soundfx_enabled
    __soundfx_enabled = not is_soundfx_enabled()


def get_FPS():
    """
    get FPS value as of resource\n
    :return:
    """
    return __FPS


def get_holdtime():
    """
    get the holdtime, that is 1 000ms / FPS\n
    :return:
    """
    return __holdtime

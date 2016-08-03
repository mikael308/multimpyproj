"""
settings access functions

:author: Mikael Holmbom
:version: 1.0
"""


__soundfx_enabled = True


def is_soundfx_enabled():
    return __soundfx_enabled


def switch_soundfx_enabled():
    """
    switch the value of setting: soundfx enabled
    :return:
    """
    __soundfx_enabled = not is_soundfx_enabled()
    print "soundfx is " + str(__soundfx_enabled)

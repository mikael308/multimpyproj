"""
functions used to modify view instances\n

:author: Mikael Holmbom
:version: 1.0
"""

import pygame


def add_shadow(surface, shadow_color, shadow_size):
    """
    add shadow to surface\n
    :param surface: the shadow to influence
    :param shadow_color: the color of the shadow part
    :param shadow_size: the size of the shadow
    :return: the surface containing shadow
    """
    w = surface.get_width()
    h = surface.get_height()
    shadow_size += -1
    pygame.draw.lines(surface, shadow_color, False,
                      ((w - shadow_size, 0),
                       (w - shadow_size, h - shadow_size),
                       (0, h - shadow_size)),
                      shadow_size + 1)

    return surface


def shift_intensiveness(color, diff):
    """
    shifts the intensiveness of a color value as of RGB\n
    does not modify param color, returns the shifted color\n
    :param color: the color value to shift
    :param diff: the difference in color intense, negative value for darker, positive for lighter
    :type diff: int
    :return: the shifted color value
    """
    new_color = []
    for v in color: # iterate r,g,b
        mod_v = v + diff
        if mod_v < 0:
            mod_v = 0
        elif mod_v > 255:
            mod_v = 255
        new_color.append(mod_v)

    return new_color

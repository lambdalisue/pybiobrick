#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
import pyx
from pyx.box import polygon
from pyx.color import cmyk
from math import sin, cos, pi

from . import Brick

class Terminator(Brick):
    _default_color = cmyk.Red
    _offset = (1, 0)
    _path = polygon([(-1*sin(i*2*pi/6), cos(i*2*pi/6)) for i in xrange(6)]).path()
    
brick_class = Terminator

if __name__ == '__main__':
    b = Terminator("Terminator")
    c = pyx.canvas.canvas()
    offset = 0
    MARGIN = 0.5
    for i in xrange(0, 3):
        offset += b.draw(c, offset) + MARGIN
    c.writeEPSfile("terminator.eps")


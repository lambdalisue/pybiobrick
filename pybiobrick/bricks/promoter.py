#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
from pyx import canvas
from pyx.path import path, moveto, lineto, curveto, closepath
from pyx.color import cmyk
from math import sqrt

from . import Brick

class Promoter(Brick):
    _default_color = cmyk.ForestGreen
    _offset = (0, -0.5)
    _path = path(
        moveto(0, 0),
        lineto(1, 0),
        lineto(1, 1),
        lineto(4, 1),
        lineto(4, 0.5),
        lineto(4+sqrt(3)*0.75, 1.25),
        lineto(4, 2.0),
        lineto(4, 1.5),
        lineto(1, 1.5),
        curveto(0.5, 1.5, 0.125, 1.5, 0, 1),
        lineto(0, 0),
        closepath()
    )
        
brick_class = Promoter

if __name__ == '__main__':
    b = Promoter("Promoter")
    c = canvas.canvas()
    offset = 0
    MARGIN = 0.5
    for i in xrange(0, 3):
        offset += b.draw(c, offset) + MARGIN
    c.writeEPSfile("promoter.eps")


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
from pyx import canvas
from pyx.path import path, moveto, lineto, closepath
from pyx.color import cmyk
from math import sqrt

from . import Brick

class ProteinDomain(Brick):
    _default_color = cmyk.Purple
    _offset = (0, -0.5)
    _path = path(
        moveto(0, 0),
        lineto(1, 0),
        lineto(1, 1),
        lineto(0, 1),
        lineto(0, 0),
        closepath(),
        moveto(1.4, 0),
        lineto(2.4, 0),
        lineto(2.4, 1),
        lineto(1.4, 1),
        lineto(1.4, 0),
        closepath(),
        moveto(2.8, 0),
        lineto(4, 0),
        lineto(4, -0.5),
        lineto(4+sqrt(3), 0.5),
        lineto(4, 1.5),
        lineto(4, 1),
        lineto(2.8, 1),
        lineto(2.8, 0),
        closepath()
    )

brick_class = ProteinDomain

if __name__ == '__main__':
    b = ProteinDomain("Protein Domain")
    c = canvas.canvas()
    offset = 0
    MARGIN = 0.5
    for i in xrange(0, 3):
        offset += b.draw(c, offset) + MARGIN
    c.writeEPSfile("protein_domain.eps")



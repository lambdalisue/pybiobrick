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

class ProteinCodingSequence(Brick):
    _default_color = cmyk.Purple
    _offset = (0, -0.5)
    _path = path(
        moveto(0, 0),
        lineto(3, 0),
        lineto(3, -0.5),
        lineto(3+sqrt(3), 0.5),
        lineto(3, 1.5),
        lineto(3, 1),
        lineto(0, 1),
        lineto(0, 0),
        closepath()
    )

brick_class = ProteinCodingSequence

if __name__ == '__main__':
    b = ProteinCodingSequence("Protein Coding Sequence")
    c = canvas.canvas()
    offset = 0
    MARGIN = 0.5
    for i in xrange(0, 3):
        offset += b.draw(c, offset) + MARGIN
    c.writeEPSfile("protein_coding_sequence.eps")


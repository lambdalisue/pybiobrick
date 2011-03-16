#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
from pyx import canvas

from . import Brick
from ribosome_binding_site import RibosomeBindingSite
from protein_coding_sequence import ProteinCodingSequence

class TranslationalUnit(Brick):
    def __init__(self, label, color=None, color2=None):
        self.label = label
        self.r = RibosomeBindingSite(None, color)
        self.p = ProteinCodingSequence(None, color2)
    
    def _path_width(self):
        return self.r._path_width() + self.p._path_width()
    def _width(self):
        return self.r._width() + self.p._width()

    def _draw_path(self, canvas, offset):
        _offset = offset + self.r.draw(canvas, offset)
        self.p.draw(canvas, _offset)

brick_class = TranslationalUnit

if __name__ == '__main__':
    b = TranslationalUnit("Translational Unit")
    c = canvas.canvas()
    offset = 0
    MARGIN = 0.5
    for i in xrange(0, 3):
        offset += b.draw(c, offset) + MARGIN
    c.writeEPSfile("translational_unit.eps")


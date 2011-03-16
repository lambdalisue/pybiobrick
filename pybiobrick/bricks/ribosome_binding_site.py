#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
from pyx import canvas, trafo
from pyx.path import circle
from pyx.color import cmyk

from . import Brick

class RibosomeBindingSite(Brick):
    _default_color = cmyk.OliveGreen
    _offset = (0, -0.8)
    
    def __init__(self, label, color=None):
        super(RibosomeBindingSite, self).__init__(label, color)
        c = circle(1, 1, 1)
        c = c.transformed(trafo.scale(sx=2, sy=0.8))
        self._path = c

brick_class = RibosomeBindingSite

if __name__ == '__main__':
    b = RibosomeBindingSite("Ribosome Binding Site")
    c = canvas.canvas()
    offset = 0
    MARGIN = 0.5
    for i in xrange(0, 3):
        offset += b.draw(c, offset) + MARGIN
    c.writeEPSfile("ribosome_binding_site.eps")


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
import pyx
from pyx.path import rect
from pyx.color import cmyk

from . import Brick

class SignalSequence(Brick):
    _default_color = cmyk.Blue
    _offset = (0, -0.5)
    _path = rect(0, 0, 3, 1)

brick_class = SignalSequence

if __name__ == '__main__':
    b = SignalSequence("Signal Sequence")
    c = pyx.canvas.canvas()
    offset = 0
    MARGIN = 0.5
    for i in xrange(0, 3):
        offset += b.draw(c, offset) + MARGIN
    c.writeEPSfile("signal_sequence.eps")


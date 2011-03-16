#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
import pyx

TEXT_Y_OFFSET = 1.7
TEXT_FONT_SIZE = pyx.text.size.LARGE

class Brick(object):
    u"""Base class of BioBrick"""
    
    # Default color
    _default_color = pyx.color.cmyk.Black

    # Brick relative offset (for regulate offset)
    _offset = (0, 0)
    # Text relative offset (for regulate offset)
    _text_offset = (0, 0)

    def __init__(self, label, color=None):
        u"""Constructor of the class

        Arguments:
            label   - the label of this brick. it will display above of brick image
            color   - the name of color or pyx.color instance. ref http://pyx.sourceforge.net/manual/colorname.html#colorname
        """
        self.label = label
        if color is None:
            color = self._default_color
        elif isinstance(color, basestring):
            color = getattr(pyx.color.cmyk, color)
        self.color = color

    def _text_width(self):
        if not self.label:
            return 0
        if not hasattr(self, '_text_width_cache'):
            # Get longest word
            longest = lambda s: max(s.split()) if ' ' in s else s
            word = longest(self.label)
            self._text_width_cache = pyx.text.text(0, 0, word, [TEXT_FONT_SIZE]).bbox().width()
        return self._text_width_cache
    def _path_width(self):
        if not hasattr(self, '_path_width_cache'):
            self._path_width_cache = self._path.bbox().width()
        return self._path_width_cache
    def _width(self):
        return max(self._text_width(), self._path_width())

    def _text(self, margin=0.25):
        if not self.label:
            return None
        if not hasattr(self, '_text_cache'):
            textattrs = [
                TEXT_FONT_SIZE,
                pyx.text.parbox(self._width()),
                pyx.text.halign.boxcenter,
                pyx.text.halign.flushcenter,
                pyx.text.valign.bottom,
            ]
            cx = self._width() / 2
            self._text_cache = pyx.text.text(cx, 0, self.label, textattrs)
        return self._text_cache

    def _draw_path(self, canvas, offset):
        x = offset + self._offset[0] + (self._width() - self._path_width()) / 2
        y = self._offset[1]
        path = self._path.transformed(pyx.trafo.translate(x, y))
        canvas.fill(path, [self.color])
        canvas.stroke(path, [pyx.style.linewidth.THIck])
    
    def _draw_text(self, canvas, offset):
        if self._text() is None:
            return
        x = offset
        y = TEXT_Y_OFFSET
        canvas.insert(self._text(), [pyx.trafo.translate(x, y)])

    def draw(self, canvas, offset):
        u"""Draw brick and label to canvas with offset

        Arguments:
            canvas  - the target canvas instance
            offset  - offset of x direction

        Return:
            pyx.length - the x-length of this brick
        """
        self._draw_path(canvas, offset)
        self._draw_text(canvas, offset)
        return self._width()

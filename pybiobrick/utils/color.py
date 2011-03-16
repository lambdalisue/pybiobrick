#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
from pyx.color import rgb, cmyk

def get(color):
    if isinstance(color, basestring):
        if color.startswith('#'):
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
            color = rgb(r=r/255.0, g=g/255.0, b=b/255.0)
        else:
            color = getattr(cmyk, color, cmyk.Black)
    return color

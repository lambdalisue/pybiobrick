#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
import pyx

def draw(canvas, bricks, margin=0.5, baseline_color=pyx.color.cmyk.Gray, baseline_thick=pyx.style.linewidth.THICk):
    u"""Draw bricks sequence to the canvas
    
    Arguments:
        canvas          - the target pyx.canvas.canvas instance
        bricks          - the list of Brick subclass instance
        margin          - the margin size of each bricks
        baseline_color  - the color of baseline (pyx.color)
        baseline_thick  - the thickness of baseline (pyx.style.linewidth)
    """
    # Calculate total width
    width = margin
    for brick in bricks:
        width += margin + brick._width()
    # Draw baseline
    canvas.stroke(pyx.path.line(0, 0, width, 0), [baseline_color, baseline_thick])
    # Draw bricks
    offset = margin
    for brick in bricks:
        offset += brick.draw(canvas, offset) + margin

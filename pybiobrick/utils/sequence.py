#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
import pyx
from color import get as c

def draw(canvas, bricks, margin=0.5, 
        baseline_color=c("#101010")):
    u"""Draw bricks sequence to the canvas
    
    Arguments:
        canvas          - the target pyx.canvas.canvas instance
        bricks          - the list of Brick subclass instance
        margin          - the margin size of each bricks
        baseline_color  - the color of baseline (pyx.color)
    """
    # Calculate total width
    width = margin
    for brick in bricks:
        width += margin + brick._width()
    # Draw baseline
    canvas.fill(pyx.path.rect(0, -0.25, width, 0.5), [baseline_color])
    # Draw bricks
    offset = margin
    for brick in bricks:
        offset += brick.draw(canvas, offset) + margin

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
import pyx
from optparse import OptionParser
from pybiobrick.utils import sequence
from pybiobrick.parser import xmlparser
from pybiobrick.parser import strparser

if __name__ == '__main__':
    usage = "usage: %prog [options] [buffer]"
    version = "%prog 0.1"
    parser = OptionParser(usage=usage, version=version)
    parser.add_option('-f', '--format', dest='format', default="string",
            help="load BioBrick sequence data as FORMAT", metavar="FORMAT")
    parser.add_option('-o', '--output', dest='output', default="output.eps",
            help="write output eps file to FILE", metavar="FILE")
    parser.add_option('-i', '--input', dest='filename', default=None,
            help="read data from FILE", metavar="FILE")
    (opts, args) = parser.parse_args()
    
    # Read
    if opts.filename:
        buf = open(opts.filename, 'r')
    elif len(args) >= 1:
        buf = args[0]
    else:
        parser.print_help()
        exit(0)

    # Parse
    if opts.format == 'string':
        bricks = strparser.parse(buf)
    elif opts.format == 'xml':
        bricks = xmlparser.parse(buf)
    else:
        parser.error("unknown format is selected.")
        exit(1)

    c = pyx.canvas.canvas()
    sequence.draw(c, bricks)
    c.writeEPSfile(opts.output)

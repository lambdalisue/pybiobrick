#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
# <?xml version="1.0" encoding="UTF-8"?>
# <root>
#   <sequence>
#     <brick color="Red">
#       <type>promoter</type>
#       <label>Promoter</label>
#     </brick>
#   </sequence>
# </root>
#

import xml.sax as sax
from xml.sax.saxutils import DefaultHandler
from ..utils import bricks

class SequenceHandler(DefaultHandler):
    def __init__(self, sequence, root='root'):
        self.sequence = sequence
        self.root = root
        self.current_node = root
        self.previous_node = None

    def startElement(self, name, attrs):
        self.previous_node = self.current_node
        self.current_node = name
        if name == 'brick':
            if 'color' in attrs.keys():
                self.current_color = attrs['color']
            else:
                self.current_color = None

    def endElement(self, name):
        self.current_node = self.previous_node
        if name == 'brick':
            self.sequence.append(bricks.brick_factory(self.current_type, self.current_label, self.current_color))

    def characters(self, char):
        if self.current_node == 'type':
            self.current_type = char
        elif self.current_node == 'label':
            self.current_label = char

def parse(string):
    sequence = []
    parser = sax.make_parser()
    parser.setFeature(sax.handler.feature_namespaces, 0)
    parser.setContentHandler(SequenceHandler(sequence))
    parser.parse(string)
    return sequence 

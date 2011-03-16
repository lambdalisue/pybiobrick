#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
import imp
import os.path


def brick_factory(module, label, color=None):
    f, filename, description = imp.find_module('pybiobrick')
    mod = imp.load_module('pybiobrick', f, filename, description)

    f, filename, description = imp.find_module('bricks', mod.__path__)
    mod = imp.load_module('pybiobrick.bricks', f, filename, description)
    
    f, filename, description = imp.find_module(module, mod.__path__)
    mod = imp.load_module('pybiobrick.bricks.%s'%module, f, filename, description)
    if f: f.close()
    return mod.brick_class(label, color)

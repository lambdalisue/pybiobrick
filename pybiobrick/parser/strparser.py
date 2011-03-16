#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
import re
from ..utils.bricks import brick_factory

BRANKET_TABLE = (
    ('[[',  '>>',   'promoter'),
    ('(',   ')',    'ribosome_binding_site'),
    ('==',  '=>',   'protein_coding_sequence'),
    ('**',  '*>',   'protein_domain'),
    ('()',  '=>',   'translational_unit'),
    ('<<',  '>>',   'terminator'),
)
PATTERN = re.compile(r"""
    \s*
    (?P<prefix>[^a-zA-Z0-9\-\{\}\\\s]+)     # Prefix operator
    \s*
    (?P<label>[a-zA-Z0-9\-\{\}\\\s#]*)       # Label
    \s*
    (?P<suffix>[^a-zA-Z0-9\-\{\}\\\s]+)     # Suffix operator
    \s*
    """, re.MULTILINE | re.VERBOSE)

def _find(prefix, suffix):
    for branket in BRANKET_TABLE:
        if (prefix, suffix) == branket[:2]:
            return branket[2]
    return None

def parse(string):
    print "parse string brick model..."
    bricks = []
    for m in PATTERN.finditer(string):
        prefix = m.group('prefix')
        label = m.group('label')
        if '#' in label:
            label, color = label.split('#', 1)
        else:
            color = None
        suffix = m.group('suffix')

        module = _find(prefix, suffix)
        if module is None:
            print "prefix: %s, suffix: %s operater is not avariable." % (prefix, suffix)
            continue
        print "prefix: %s\tsuffix: %s\t => module: %s" % (prefix, suffix, module)


        bricks.append(brick_factory(module, label, color))

    return bricks

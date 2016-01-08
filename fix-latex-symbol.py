#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function

import os
import sys
from pandocfilters import toJSONFilter, Math
import json


def fix_latex_symbol(key, value, format, meta):

    print(key, value, format, meta, file=sys.stderr)

    if key == 'RawInline':
        if value[1] == '\\LaTeX':
            return Math({u'c': [], u't': u'InlineMath'}, u'\\LaTeX')


if __name__ == "__main__":
    toJSONFilter(fix_latex_symbol)


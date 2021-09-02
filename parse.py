#!/usr/bin/env python3

"""
TBD
"""

import logging
import json
import re
import sys
from enum import Enum

class InputFileFormat(Enum):
#    CONFIG = r'^\s*config\s+(system|switch|router){1}\s+(\S+)\s*$'
    # liste de mots clés à définir... en attendant, je prends n'importe quoi après le config
#    CONFIG = r'^\s*config\s+(system|switch|router|redistribute|redistribute6){1}\s+.*'
    CONFIG = r'^\s*config\s+(\S+){1}.*'
#    EDIT = r'^\s*edit\s+(\S+)\s*$'
    EDIT = r'^\s*edit\s+.*'
    # pour le SET, je ne prends pas en compte le multiline
    SET = r'^\s*set\s+.*'
    UNSET = r'^\s*unset\s+.*'
    NEXT = r'^\s*next\s*$'
    END = r'^\s*end\s*$'


if __name__  ==  '__main__':
    with open('./test-yann.conf', 'r', encoding='utf-8') as config:
        data = [ l.strip() for l in config.readlines()]

    for line in data:
        #print(line)
        if re.match(InputFileFormat.CONFIG.value, line):
            continue
            #print('config => {}'.format(line))
        if re.match(InputFileFormat.EDIT.value, line):
            continue
            #print('edit ====> {}'.format(line))
        if re.match(InputFileFormat.SET.value, line):
            continue
            #print('    set ============> {}'.format(line))
        if re.match(InputFileFormat.UNSET.value, line):
            continue
            #print('    set ============> {}'.format(line))
        if re.match(InputFileFormat.NEXT.value, line):
            continue
            #print('next =========> {}'.format(line))
        if re.match(InputFileFormat.END.value, line):
            continue
            #print('end ============> {}'.format(line))
        print(line)
    sys.exit(0)

sys.exit(0)

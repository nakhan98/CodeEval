#!/usr/bin/env python2
# CodeEval - File Size
# https://www.codeeval.com/open_challenges/26/

import os
import sys

print( os.stat(sys.argv[1]).st_size )

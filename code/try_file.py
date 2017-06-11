#!/usr/bin/env python3

f = open('/etc/hosts', 'r' ,encoding='utf-8')
try:
    for line in f:
        if 'apu' in line:
            print(line)
finally:
    # always called
    f.close()

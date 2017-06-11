#!/usr/bin/env python3

with open('/etc/hosts', 'r', encoding='utf-8') as f:
    print(f, '\n')
    for line in f:
        if 'apu' in line:
            print(line)

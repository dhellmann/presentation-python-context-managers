#!/bin/bash

set -x

FILES="*.html css js lib plugin img fonts"

ssh doughellmann.com 'mkdir -p ~/doughellmann.com/presentations/python-context-managers'

rsync -av --progress $FILES doughellmann.com:~/doughellmann.com/presentations/python-context-managers/

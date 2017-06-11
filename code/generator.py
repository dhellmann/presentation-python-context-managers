#!/usr/bin/env python

"""Defining your own context manager with a generator function
"""

import contextlib

@contextlib.contextmanager
def my_context():
    print 'entering my_context'
    try:
        yield 'something'
    except RuntimeError:
        print 'handled'
    print 'exiting my_context'

print
with my_context() as msg:
    try:
        print 'Doing work in the context "%s"' % msg
        raise RuntimeError('hi again')
    except RuntimeError:
        print 'error'
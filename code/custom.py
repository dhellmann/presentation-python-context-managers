#!/usr/bin/env python

"""Defining your own context manager.
"""

class MyContext(object):
    def __init__(self):
        print '__init__()'
    
    def __enter__(self):
        print '__enter__() (acquire the resource)'
        return 5
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__() (release the resource)'
        print str(exc_val)
        return True

print
with MyContext() as c:
    print 'Doing work in the context', c
    raise RuntimeError('hi!')
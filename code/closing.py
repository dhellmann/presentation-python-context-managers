import contextlib

class MyClosable(object):
    def __init__(self):
        print('init')

    def open(self):
        print('open')
        return self

    def close(self):
        print('close')

with contextlib.closing(MyClosable().open()) as f:
    print('working with', f)

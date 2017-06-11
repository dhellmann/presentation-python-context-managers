import contextlib

@contextlib.contextmanager
def my_context():
    print('entering my_context')
    try:
        yield 'something'
    except RuntimeError:
        print('handled error in context manager')
    print('exiting my_context')

with my_context() as msg:
    raise ValueError('fails again')

class MyContext(object):

    def __enter__(self):
        return 5

    def __exit__(self, exc_type, exc_val, exc_tb):
        if issubclass(exc_type, RuntimeError):
            print('Handling exception:', exc_val)
            return True
        print('Unhandled Exception:', exc_val)

with MyContext() as c:
    raise RuntimeError('this is OK')

with MyContext() as c:
    raise ValueError('this causes failure')

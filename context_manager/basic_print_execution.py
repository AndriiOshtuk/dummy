""" Simple context manager example that prints execution path"""


class ContextManager:

    def __enter__(self):
        print('__enter__')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')


with ContextManager() as s:
    print('User code')

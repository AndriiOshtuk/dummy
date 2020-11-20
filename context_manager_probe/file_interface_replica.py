""" Simple context manager example that prints execution path"""

from pathlib import Path


class ContextManager:

    def __init__(self, filename):
        print('__init__')
        self.file = open(filename)

    def __enter__(self):
        print('__enter__')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        print(f'{exc_type}: {exc_val}')
        self.file.close()
        return True


with ContextManager(Path(__file__)) as s:
    print(s.readlines())
    raise EOFError

print('Script end')


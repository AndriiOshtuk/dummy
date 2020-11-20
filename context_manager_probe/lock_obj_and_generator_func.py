from contextlib import contextmanager


class Lock:
    def __init__(self):
        self.locked = False

    def lock(self):
        self.locked = True

    def release(self):
        self.locked = False


@contextmanager
def locked(lock):
    lock.lock()
    try:
        yield
    finally:
        lock.release()

l = Lock()
l.lock()
with locked(l):
    print('Run code')
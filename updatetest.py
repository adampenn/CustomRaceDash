class Stopwatch(object):
    def __init__(self, callback):
        self._stop = False
        self.callback = callback

    @property
    def stop(self): return self._stop

    @stop.setter
    def stop(self, value):
        self._stop = value
        if value: self.callback()



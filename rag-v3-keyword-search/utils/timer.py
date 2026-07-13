import time


class Timer:
    """
    Measures execution time.
    """

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        """
        Starts the timer.
        """
        self.start_time = time.perf_counter()

    def stop(self):
        """
        Stops the timer.
        """
        self.end_time = time.perf_counter()

    @property
    def elapsed(self):
        """
        Returns elapsed execution time.
        """
        return self.end_time - self.start_time